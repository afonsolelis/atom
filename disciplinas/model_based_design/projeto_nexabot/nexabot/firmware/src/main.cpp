/*
 * main.cpp — firmware do alvo HIL real (ESP32) do NexaBot.
 *
 * NÃO COMPILÁVEL NESTE AMBIENTE: requer PlatformIO + toolchain Xtensa
 * instalados na máquina do estudante (ver platformio.ini nesta pasta).
 * O código abaixo é sintaticamente correto e seria compilado/gravado com
 *
 *     pio run -t upload
 *     pio device monitor -b 115200
 *
 * O protocolo de linha pela UART é EXATAMENTE o mesmo do back-end que
 * roda de verdade neste ambiente sem hardware, `LoopbackTarget`
 * (nexabot/hil.py + nexabot/firmware/main_loopback.c): comandos
 * "STEP r y [delay_ms]" / "RESET" / "QUIT", respostas "U u" / "OK" — por
 * isso o mesmo `nexabot.hil.run_closed_loop_hil` funciona sem alteração
 * ao trocar `LoopbackTarget` por `SerialTarget(port="/dev/ttyUSB0")`.
 *
 * O núcleo PID (struct + pid_init/pid_reset/pid_step) abaixo é uma CÓPIA
 * SINCRONIZADA à mão da variante em double gerada pela Aula 13
 * (nexabot/codegen/generated/pid_controller.{h,c}) — o mesmo contrato
 * numérico de `DiscretePID.step` (nexabot/controllers.py), reescrito em
 * C++ porque um `.ino`/`.cpp` do Arduino framework não inclui arquivos
 * gerados fora da árvore `src/` sem configuração extra de build. Ao
 * mudar os ganhos do modelo, regenere com
 *
 *     .venv/bin/python -m nexabot.codegen.generate
 *
 * e copie o novo `pid_step`/`pid_init` para cá (ou, em uma esteira de CI
 * real, adicione um passo que copie automaticamente
 * nexabot/codegen/generated/pid_controller.* para nexabot/firmware/src/
 * antes de `pio run` — deixado como exercício de integração contínua).
 */
#include <Arduino.h>

typedef struct {
    double Kp, Ki, Kd, Ts, u_max, tau_f, Kaw;
    double integral, e_prev, d_state;
} pid_controller_t;

static void pid_reset(pid_controller_t *pid)
{
    pid->integral = 0.0;
    pid->e_prev = 0.0;
    pid->d_state = 0.0;
}

static void pid_init(pid_controller_t *pid, double Kp, double Ki, double Kd,
                      double Ts, double u_max, double tau_f, double Kaw)
{
    pid->Kp = Kp;
    pid->Ki = Ki;
    pid->Kd = Kd;
    pid->Ts = Ts;
    pid->u_max = u_max;
    pid->tau_f = tau_f;
    pid->Kaw = Kaw;
    pid_reset(pid);
}

/* Contrato numérico idêntico ao de DiscretePID.step / pid_step (SIL):
 *   e[k]   = r[k] - y[k]
 *   I[k]   = I[k-1] + Ki.Ts.e[k]
 *   D[k]   = (Kd.(e[k]-e[k-1]) + tau_f.D[k-1]) / (tau_f + Ts)
 *   u_ns   = Kp.e[k] + I[k] + D[k]
 *   u[k]   = sat(u_ns, -u_max, +u_max)
 *   se u[k] != u_ns:  I[k] <- I[k] + Kaw.(u[k] - u_ns).Ts
 */
static double pid_step(pid_controller_t *pid, double r, double y)
{
    double e = r - y;
    pid->integral += pid->Ki * pid->Ts * e;

    double d = (pid->Kd * (e - pid->e_prev) + pid->tau_f * pid->d_state) /
               (pid->tau_f + pid->Ts);

    double u_unsat = pid->Kp * e + pid->integral + d;
    double u = u_unsat;
    if (u > pid->u_max) {
        u = pid->u_max;
    } else if (u < -pid->u_max) {
        u = -pid->u_max;
    }
    if (u != u_unsat) {
        pid->integral += pid->Kaw * (u - u_unsat) * pid->Ts;
    }

    pid->e_prev = e;
    pid->d_state = d;
    return u;
}

/* Ganhos do eixo de tração (ver nexabot/params.py e nexabot/controllers.py
 * para a sintonia de referência). Trocar aqui exige recompilar e regravar
 * -- em um sistema de produção, viriam de uma tabela de calibração na
 * flash, não de uma constante de compilação. */
static pid_controller_t g_pid;
static const double KP = 2.0, KI = 40.0, KD = 0.02;
static const double TS = 0.005, U_MAX = 24.0, TAU_F = 0.01, KAW = 1.0;

static String g_line;

void setup()
{
    Serial.begin(115200);
    while (!Serial) {
        delay(10);
    }
    pid_init(&g_pid, KP, KI, KD, TS, U_MAX, TAU_F, KAW);
    g_line.reserve(128);
}

static void handle_line(const String &line)
{
    if (line.startsWith("STEP")) {
        double r = 0.0, y = 0.0, delay_ms = 0.0;
        int n = sscanf(line.c_str() + 4, "%lf %lf %lf", &r, &y, &delay_ms);
        if (n < 2) {
            Serial.println("ERR linha STEP malformada");
            return;
        }
        double u = pid_step(&g_pid, r, y);
        if (delay_ms > 0.0) {
            delay((unsigned long)delay_ms);
        }
        Serial.print("U ");
        Serial.println(u, 10);
    } else if (line.startsWith("RESET")) {
        pid_reset(&g_pid);
        Serial.println("OK");
    } else if (line.startsWith("QUIT")) {
        /* Em um alvo real não há "sair" -- ignora e continua servindo. */
    } else {
        Serial.println("ERR comando desconhecido");
    }
}

void loop()
{
    while (Serial.available() > 0) {
        char c = (char)Serial.read();
        if (c == '\n') {
            handle_line(g_line);
            g_line = "";
        } else if (c != '\r') {
            g_line += c;
        }
    }
}
