/* ============================================================================
 * ARQUIVO GERADO AUTOMATICAMENTE — NÃO EDITAR MANUALMENTE
 *
 * Qualquer edição manual será perdida na próxima geração e quebra a
 * cadeia de rastreabilidade requisito -> modelo -> código -> teste
 * (ver nexabot/rastreabilidade.py e rastreabilidade.md).
 *
 * Requisitos de origem   : REQ-CTRL-001, REQ-CTRL-002, REQ-CTRL-003, REQ-CODEGEN-001, REQ-CODEGEN-002
 * Modelo de referência   : nexabot.controllers.DiscretePID (pacote nexabot v1.0.0)
 * Gerador                : nexabot/codegen/generate.py + templates Jinja2 (pid_controller.c.h.j2)
 * Parâmetros do modelo   : Kp=2.0, Ki=40.0, Kd=0.02, Ts=0.005, u_max=24.0, tau_f=0.01, Kaw=1.0
 * Hash SHA-256 (params)  : dc3b95c3d13a052d4dee683c2d5cd75bbc3c3996dede09f747dc8c076c32fa13
 * Gerado em (UTC)        : 2026-08-29T23:56:04Z
 *
 * Equações derivadas simbolicamente por SymPy a partir da forma
 * contínua do PID (Kp + Ki/s + Kd.s/(1+tau_f.s)), via discretização
 * de Euler para trás (ver nexabot/codegen/derive.py):
 *   I[k] = I[k-1] + Ki*Ts*e[k]
 *   D[k] = (Kd*(e[k]-e[k-1]) + tau_f*D[k-1]) / (tau_f + Ts)
 ============================================================================= */
#ifndef PID_CONTROLLER_H_
#define PID_CONTROLLER_H_

/*
 * PID discreto do NexaBot — cabeçalho gerado.
 *
 * Portável para microcontrolador: sem malloc, sem dependência de libc além
 * de <stdint.h>/<math.h> (apenas para NAN em depuração, não usada em
 * runtime), estado inteiramente contido em uma struct por instância.
 *
 * Duas variantes são geradas:
 *   - pid_controller_t / pid_*        -> aritmética em double (referência)
 *   - pid_fixed_controller_t / pid_fixed_* -> ponto fixo Q16.16 (embarcado
 *     sem FPU); ver `pid_controller.c` para a análise de quantização.
 *
 * A variante em uso é escolhida pelo firmware que inclui este cabeçalho
 * (ver `nexabot/firmware/main_loopback.c`), não por este arquivo.
 */

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/* ---------------------------------------------------------------------
 * Variante em ponto flutuante (double) — reproduz DiscretePID.step bit
 * a bit (a menos de erro de arredondamento IEEE-754, o mesmo que o
 * Python/NumPy usam).
 * ------------------------------------------------------------------- */
typedef struct {
    /* Ganhos e parâmetros (constantes após pid_init) */
    double Kp;
    double Ki;
    double Kd;
    double Ts;
    double u_max;
    double tau_f;
    double Kaw;

    /* Estado interno (mutável a cada pid_step) */
    double integral;
    double e_prev;
    double d_state;
} pid_controller_t;

/* Inicializa a struct com os ganhos/parâmetros do modelo e zera o estado. */
void pid_init(pid_controller_t *pid, double Kp, double Ki, double Kd,
              double Ts, double u_max, double tau_f, double Kaw);

/* Zera o estado interno (integral, e_prev, d_state). REQ-SAFE-004. */
void pid_reset(pid_controller_t *pid);

/* Executa um passo de controle e devolve a tensão de comando u[k] [V]. */
double pid_step(pid_controller_t *pid, double r, double y);

/* ---------------------------------------------------------------------
 * Variante em ponto fixo Q16.16 (16 bits inteiros, 16 bits fracionários,
 * em um int32_t). Selecionável em alvos sem unidade de ponto flutuante.
 * ------------------------------------------------------------------- */
typedef int32_t pid_fixed_t;

#define PID_FIXED_SHIFT 16
#define PID_FIXED_ONE   ((pid_fixed_t)1 << PID_FIXED_SHIFT)

/* Conversões entre double (host/estudo) e Q16.16 (alvo). Não usadas no
 * laço de controle do alvo real — só para inicializar ganhos a partir de
 * valores calculados em ponto flutuante e para depuração. */
pid_fixed_t pid_double_to_fixed(double x);
double pid_fixed_to_double(pid_fixed_t x);

typedef struct {
    pid_fixed_t Kp;
    pid_fixed_t Ki;
    pid_fixed_t Kd;
    pid_fixed_t Ts;
    pid_fixed_t u_max;
    pid_fixed_t tau_f;
    pid_fixed_t Kaw;

    pid_fixed_t integral;
    pid_fixed_t e_prev;
    pid_fixed_t d_state;
} pid_fixed_controller_t;

void pid_fixed_init(pid_fixed_controller_t *pid, double Kp, double Ki,
                     double Kd, double Ts, double u_max, double tau_f,
                     double Kaw);
void pid_fixed_reset(pid_fixed_controller_t *pid);
pid_fixed_t pid_fixed_step(pid_fixed_controller_t *pid, pid_fixed_t r,
                            pid_fixed_t y);

#ifdef __cplusplus
}
#endif

#endif /* PID_CONTROLLER_H_ */
