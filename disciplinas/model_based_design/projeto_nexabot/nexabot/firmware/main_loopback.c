/*
 * main_loopback.c — "alvo" HIL rodando como processo local.
 *
 * Este é o back-end LoopbackTarget de nexabot/hil.py (Aula 15): em vez de
 * UART real, troca linhas de texto por stdin/stdout com o processo host
 * (a planta, simulada em Python). O laço de leitura/parsing/resposta é
 * IDÊNTICO ao do firmware ESP32 real (ver src/main.cpp) — só o meio de
 * transporte muda (stdin/stdout aqui, UART lá) — por isso este executável
 * é um gêmeo de simulação legítimo do alvo embarcado, não um mock.
 *
 * Protocolo de linha (um comando ASCII por linha, terminado em '\n'):
 *
 *   host -> alvo:  "STEP <r> <y> [delay_ms]"
 *                      pede um passo de controle; o campo opcional
 *                      delay_ms injeta um atraso proposital de resposta
 *                      (nanosleep) — usado na Aula 15 para demonstrar um
 *                      watchdog reagindo a um alvo lento de verdade.
 *   host -> alvo:  "RESET"          zera o estado do controlador
 *   host -> alvo:  "QUIT"           encerra o processo
 *   alvo -> host:  "U <u>"          resposta a STEP, tensão de comando [V]
 *   alvo -> host:  "OK"             resposta a RESET
 *
 * O núcleo de controle (pid_controller.c, gerado pela Aula 13) não faz
 * nenhum printf/malloc — só este laço de protocolo, que existe apenas
 * para a demonstração HIL, usa E/S.
 *
 * Uso: main_loopback <Kp> <Ki> <Kd> <Ts> <u_max> <tau_f> <Kaw>
 */
#define _POSIX_C_SOURCE 200809L /* expõe nanosleep() com -std=c11 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "pid_controller.h"

static void sleep_ms(double delay_ms)
{
    if (delay_ms <= 0.0) {
        return;
    }
    struct timespec ts;
    ts.tv_sec = (time_t)(delay_ms / 1000.0);
    ts.tv_nsec = (long)((delay_ms - (double)ts.tv_sec * 1000.0) * 1.0e6);
    nanosleep(&ts, NULL);
}

int main(int argc, char **argv)
{
    if (argc != 8) {
        fprintf(stderr,
                "uso: %s Kp Ki Kd Ts u_max tau_f Kaw\n", argv[0]);
        return 1;
    }

    double Kp = atof(argv[1]);
    double Ki = atof(argv[2]);
    double Kd = atof(argv[3]);
    double Ts = atof(argv[4]);
    double u_max = atof(argv[5]);
    double tau_f = atof(argv[6]);
    double Kaw = atof(argv[7]);

    pid_controller_t pid;
    pid_init(&pid, Kp, Ki, Kd, Ts, u_max, tau_f, Kaw);

    /* Sem buffer de bloco: cada linha escrita chega ao host imediatamente,
     * como aconteceria por UART. */
    setvbuf(stdout, NULL, _IOLBF, 0);

    char line[256];
    while (fgets(line, sizeof(line), stdin) != NULL) {
        if (strncmp(line, "STEP", 4) == 0) {
            double r = 0.0, y = 0.0, delay_ms = 0.0;
            int nf = sscanf(line + 4, "%lf %lf %lf", &r, &y, &delay_ms);
            if (nf < 2) {
                fprintf(stderr, "ERR linha STEP malformada: %s", line);
                continue;
            }
            double u = pid_step(&pid, r, y);
            sleep_ms(delay_ms);
            printf("U %.17g\n", u);
        } else if (strncmp(line, "RESET", 5) == 0) {
            pid_reset(&pid);
            printf("OK\n");
        } else if (strncmp(line, "QUIT", 4) == 0) {
            break;
        } else {
            fprintf(stderr, "ERR comando desconhecido: %s", line);
        }
    }
    return 0;
}
