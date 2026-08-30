/*
 * plant_fmu.c — FMU FMI 3.0 (Co-Simulation) da planta de tracao do NexaBot.
 *
 * Disciplina: Model-Based Design for Cyber-Physical Systems — Aula 8
 * "Co-simulacao planta-controlador com FMI 3.0".
 *
 * Este arquivo encapsula, em C puro, EXATAMENTE as mesmas equacoes e os
 * mesmos parametros de `nexabot/plant.py` (motor CC de tracao do NexaBot):
 *
 *     L . di/dt = V - R.i - Ke.w
 *     J . dw/dt = Kt.i - b.w - tau_load
 *
 * com x = [i, w], entradas u_volts=V e tau_load, saida principal w (omega).
 * O integrador interno e um Runge-Kutta de 4a ordem de passo fixo (mesma
 * formula usada em `plant.simulate`), sub-dividido em micro-passos quando o
 * passo de comunicacao H solicitado pelo mestre de co-simulacao (fmi3DoStep)
 * for maior que MICRO_DT — e assim que um FMU real "esconde" um solver fino
 * atras de uma interface de passo grosso.
 *
 * Implementa a interface FMI 3.0 de Co-Simulation completa exigida pelo
 * carregamento dinamico do fmpy (que resolve TODOS os simbolos de
 * `fmpy.fmi3._FMU3`/`FMU3Slave` via dlsym, mesmo os que uma FMU somente-CS
 * nunca chega a invocar) — por isso o arquivo tambem traz stubs honestos
 * (retornam fmi3Error/fmi3OK conforme o caso) para as funcoes de Model
 * Exchange, Scheduled Execution, Clocks e serializacao de estado, que este
 * FMU nao suporta.
 *
 * Rastreabilidade: REQ-PLANT-001 (equacoes da planta), REQ-PLANT-002
 * (limite de tensao V_max).
 */

#include "fmi3Functions.h"

#include <math.h>
#include <stdlib.h>
#include <string.h>

/* ------------------------------------------------------------------ */
/* Parametros do NexaBot — identicos a nexabot/params.py (PARAMS)      */
/* ------------------------------------------------------------------ */
#define P_R    1.2      /* resistencia de armadura [ohm] */
#define P_L    3.5e-3   /* indutancia de armadura [H] */
#define P_KE   0.045    /* constante de f.c.e.m. [V.s/rad] */
#define P_KT   0.045    /* constante de torque [N.m/A] */
#define P_J    2.5e-4   /* inercia motor+redutor+carga [kg.m^2] */
#define P_B    8.0e-5   /* atrito viscoso [N.m.s/rad] */
#define P_VMAX 24.0     /* tensao maxima do driver [V] */

/* Micro-passo fixo do integrador RK4 interno [s]. Independente do passo de
 * comunicacao H: se H > MICRO_DT, fmi3DoStep sub-divide internamente. */
#define MICRO_DT 5.0e-5

/* Value references (devem bater com nexabot/fmu/modelDescription.xml) */
#define VR_U_VOLTS  0u
#define VR_TAU_LOAD 1u
#define VR_OMEGA    2u
#define VR_CURRENT  3u
#define VR_TIME     4u  /* variavel independente exigida pela FMI 3.0 */

/* ------------------------------------------------------------------ */
/* Estado da instancia do FMU                                          */
/* ------------------------------------------------------------------ */
typedef struct {
    double i;         /* corrente de armadura [A] — estado */
    double w;          /* velocidade angular do motor [rad/s] — estado */
    double u_volts;    /* entrada: tensao aplicada [V] (mantida via ZOH) */
    double tau_load;   /* entrada: torque de carga [N.m] (mantida via ZOH) */
    double time;       /* tempo de simulacao corrente [s] */
    char   instanceName[256];
} ModelInstance;

/* Derivada de estado dx/dt, identica a nexabot/plant.py:derivative(). */
static void derivative(double i, double w, double u, double tau_load,
                        double *di, double *dw) {
    *di = (u - P_R * i - P_KE * w) / P_L;
    *dw = (P_KT * i - P_B * w - tau_load) / P_J;
}

/* Um passo de RK4 de tamanho h, com entradas mantidas constantes (ZOH)
 * durante o passo — mesma logica de nexabot/plant.py:simulate(). */
static void rk4_step(ModelInstance *m, double h) {
    double u = m->u_volts;
    if (u > P_VMAX) u = P_VMAX;
    if (u < -P_VMAX) u = -P_VMAX;
    double tl = m->tau_load;

    double i0 = m->i, w0 = m->w;
    double k1i, k1w, k2i, k2w, k3i, k3w, k4i, k4w;

    derivative(i0, w0, u, tl, &k1i, &k1w);
    derivative(i0 + 0.5 * h * k1i, w0 + 0.5 * h * k1w, u, tl, &k2i, &k2w);
    derivative(i0 + 0.5 * h * k2i, w0 + 0.5 * h * k2w, u, tl, &k3i, &k3w);
    derivative(i0 + h * k3i, w0 + h * k3w, u, tl, &k4i, &k4w);

    m->i = i0 + (h / 6.0) * (k1i + 2.0 * k2i + 2.0 * k3i + k4i);
    m->w = w0 + (h / 6.0) * (k1w + 2.0 * k2w + 2.0 * k3w + k4w);
}

/* ==================================================================== */
/* Common Functions                                                      */
/* ==================================================================== */

const char* fmi3GetVersion(void) {
    return "3.0";
}

fmi3Status fmi3SetDebugLogging(fmi3Instance instance,
                                fmi3Boolean loggingOn,
                                size_t nCategories,
                                const fmi3String categories[]) {
    (void) instance; (void) loggingOn; (void) nCategories; (void) categories;
    return fmi3OK; /* nenhuma categoria de log implementada */
}

/* ---- Criacao e destruicao de instancias ----------------------------- */

fmi3Instance fmi3InstantiateModelExchange(
    fmi3String instanceName, fmi3String instantiationToken,
    fmi3String resourcePath, fmi3Boolean visible, fmi3Boolean loggingOn,
    fmi3InstanceEnvironment instanceEnvironment,
    fmi3LogMessageCallback logMessage) {
    (void) instanceName; (void) instantiationToken; (void) resourcePath;
    (void) visible; (void) loggingOn; (void) instanceEnvironment; (void) logMessage;
    return NULL; /* este FMU so implementa Co-Simulation */
}

fmi3Instance fmi3InstantiateCoSimulation(
    fmi3String instanceName,
    fmi3String instantiationToken,
    fmi3String resourcePath,
    fmi3Boolean visible,
    fmi3Boolean loggingOn,
    fmi3Boolean eventModeUsed,
    fmi3Boolean earlyReturnAllowed,
    const fmi3ValueReference requiredIntermediateVariables[],
    size_t nRequiredIntermediateVariables,
    fmi3InstanceEnvironment instanceEnvironment,
    fmi3LogMessageCallback logMessage,
    fmi3IntermediateUpdateCallback intermediateUpdate) {

    (void) instantiationToken; (void) resourcePath; (void) visible;
    (void) loggingOn; (void) eventModeUsed;
    (void) requiredIntermediateVariables; (void) nRequiredIntermediateVariables;
    (void) instanceEnvironment; (void) logMessage; (void) intermediateUpdate;

    if (earlyReturnAllowed) {
        /* nao suportado: este e um FMU de co-simulacao simples, sem
         * retorno antecipado de fmi3DoStep. Segue instanciando mesmo
         * assim, pois o mestre simplesmente nao usara esse recurso. */
    }

    ModelInstance *m = (ModelInstance *) calloc(1, sizeof(ModelInstance));
    if (!m) return NULL;

    m->i = 0.0;
    m->w = 0.0;
    m->u_volts = 0.0;
    m->tau_load = 0.0;
    m->time = 0.0;

    if (instanceName) {
        strncpy(m->instanceName, instanceName, sizeof(m->instanceName) - 1);
    }

    return (fmi3Instance) m;
}

fmi3Instance fmi3InstantiateScheduledExecution(
    fmi3String instanceName, fmi3String instantiationToken,
    fmi3String resourcePath, fmi3Boolean visible, fmi3Boolean loggingOn,
    fmi3InstanceEnvironment instanceEnvironment,
    fmi3LogMessageCallback logMessage,
    fmi3ClockUpdateCallback clockUpdate,
    fmi3LockPreemptionCallback lockPreemption,
    fmi3UnlockPreemptionCallback unlockPreemption) {
    (void) instanceName; (void) instantiationToken; (void) resourcePath;
    (void) visible; (void) loggingOn; (void) instanceEnvironment;
    (void) logMessage; (void) clockUpdate; (void) lockPreemption; (void) unlockPreemption;
    return NULL; /* Scheduled Execution nao suportado */
}

void fmi3FreeInstance(fmi3Instance instance) {
    if (instance) free(instance);
}

/* ---- Modos de inicializacao, terminacao e reset ---------------------- */

fmi3Status fmi3EnterInitializationMode(fmi3Instance instance,
                                        fmi3Boolean toleranceDefined,
                                        fmi3Float64 tolerance,
                                        fmi3Float64 startTime,
                                        fmi3Boolean stopTimeDefined,
                                        fmi3Float64 stopTime) {
    (void) toleranceDefined; (void) tolerance; (void) stopTimeDefined; (void) stopTime;
    ModelInstance *m = (ModelInstance *) instance;
    if (!m) return fmi3Error;
    m->time = startTime;
    return fmi3OK;
}

fmi3Status fmi3ExitInitializationMode(fmi3Instance instance) {
    return instance ? fmi3OK : fmi3Error;
}

fmi3Status fmi3EnterEventMode(fmi3Instance instance) {
    (void) instance;
    return fmi3OK; /* nao ha eventos de estado neste modelo continuo */
}

fmi3Status fmi3Terminate(fmi3Instance instance) {
    return instance ? fmi3OK : fmi3Error;
}

fmi3Status fmi3Reset(fmi3Instance instance) {
    ModelInstance *m = (ModelInstance *) instance;
    if (!m) return fmi3Error;
    m->i = 0.0;
    m->w = 0.0;
    m->u_volts = 0.0;
    m->tau_load = 0.0;
    m->time = 0.0;
    return fmi3OK;
}

/* ==================================================================== */
/* Leitura e escrita de variaveis — apenas Float64 e suportado           */
/* ==================================================================== */

fmi3Status fmi3GetFloat64(fmi3Instance instance,
                           const fmi3ValueReference valueReferences[],
                           size_t nValueReferences,
                           fmi3Float64 values[],
                           size_t nValues) {
    ModelInstance *m = (ModelInstance *) instance;
    if (!m || nValueReferences != nValues) return fmi3Error;

    for (size_t k = 0; k < nValueReferences; k++) {
        switch (valueReferences[k]) {
            case VR_U_VOLTS:  values[k] = m->u_volts;  break;
            case VR_TAU_LOAD: values[k] = m->tau_load; break;
            case VR_OMEGA:    values[k] = m->w;        break;
            case VR_CURRENT:  values[k] = m->i;        break;
            case VR_TIME:     values[k] = m->time;     break;
            default: return fmi3Error;
        }
    }
    return fmi3OK;
}

fmi3Status fmi3SetFloat64(fmi3Instance instance,
                           const fmi3ValueReference valueReferences[],
                           size_t nValueReferences,
                           const fmi3Float64 values[],
                           size_t nValues) {
    ModelInstance *m = (ModelInstance *) instance;
    if (!m || nValueReferences != nValues) return fmi3Error;

    for (size_t k = 0; k < nValueReferences; k++) {
        switch (valueReferences[k]) {
            case VR_U_VOLTS:  m->u_volts = values[k];  break;
            case VR_TAU_LOAD: m->tau_load = values[k]; break;
            case VR_OMEGA:
            case VR_CURRENT:
                return fmi3Error; /* saidas nao sao graváveis pelo mestre */
            default: return fmi3Error;
        }
    }
    return fmi3OK;
}

/* ---- Stubs honestos: nenhuma variavel destes tipos existe neste FMU -- */

#define STUB_GETTER(NAME, TYPE)                                            \
    fmi3Status NAME(fmi3Instance instance,                                 \
                     const fmi3ValueReference valueReferences[],           \
                     size_t nValueReferences, TYPE values[],               \
                     size_t nValues) {                                     \
        (void) instance; (void) valueReferences; (void) nValueReferences;  \
        (void) values; (void) nValues;                                     \
        return fmi3Error;                                                  \
    }

#define STUB_SETTER(NAME, TYPE)                                            \
    fmi3Status NAME(fmi3Instance instance,                                 \
                     const fmi3ValueReference valueReferences[],           \
                     size_t nValueReferences, const TYPE values[],         \
                     size_t nValues) {                                     \
        (void) instance; (void) valueReferences; (void) nValueReferences;  \
        (void) values; (void) nValues;                                     \
        return fmi3Error;                                                  \
    }

STUB_GETTER(fmi3GetFloat32, fmi3Float32)
STUB_GETTER(fmi3GetInt8, fmi3Int8)
STUB_GETTER(fmi3GetUInt8, fmi3UInt8)
STUB_GETTER(fmi3GetInt16, fmi3Int16)
STUB_GETTER(fmi3GetUInt16, fmi3UInt16)
STUB_GETTER(fmi3GetInt32, fmi3Int32)
STUB_GETTER(fmi3GetUInt32, fmi3UInt32)
STUB_GETTER(fmi3GetInt64, fmi3Int64)
STUB_GETTER(fmi3GetUInt64, fmi3UInt64)
STUB_GETTER(fmi3GetBoolean, fmi3Boolean)
STUB_GETTER(fmi3GetString, fmi3String)

STUB_SETTER(fmi3SetFloat32, fmi3Float32)
STUB_SETTER(fmi3SetInt8, fmi3Int8)
STUB_SETTER(fmi3SetUInt8, fmi3UInt8)
STUB_SETTER(fmi3SetInt16, fmi3Int16)
STUB_SETTER(fmi3SetUInt16, fmi3UInt16)
STUB_SETTER(fmi3SetInt32, fmi3Int32)
STUB_SETTER(fmi3SetUInt32, fmi3UInt32)
STUB_SETTER(fmi3SetInt64, fmi3Int64)
STUB_SETTER(fmi3SetUInt64, fmi3UInt64)
STUB_SETTER(fmi3SetBoolean, fmi3Boolean)
STUB_SETTER(fmi3SetString, fmi3String)

#undef STUB_GETTER
#undef STUB_SETTER

fmi3Status fmi3GetBinary(fmi3Instance instance,
                          const fmi3ValueReference valueReferences[],
                          size_t nValueReferences,
                          size_t valueSizes[],
                          fmi3Binary values[],
                          size_t nValues) {
    (void) instance; (void) valueReferences; (void) nValueReferences;
    (void) valueSizes; (void) values; (void) nValues;
    return fmi3Error;
}

fmi3Status fmi3SetBinary(fmi3Instance instance,
                          const fmi3ValueReference valueReferences[],
                          size_t nValueReferences,
                          const size_t valueSizes[],
                          const fmi3Binary values[],
                          size_t nValues) {
    (void) instance; (void) valueReferences; (void) nValueReferences;
    (void) valueSizes; (void) values; (void) nValues;
    return fmi3Error;
}

fmi3Status fmi3GetClock(fmi3Instance instance,
                         const fmi3ValueReference valueReferences[],
                         size_t nValueReferences,
                         fmi3Clock values[]) {
    (void) instance; (void) valueReferences; (void) nValueReferences; (void) values;
    return fmi3Error; /* sem clocks neste modelo */
}

fmi3Status fmi3SetClock(fmi3Instance instance,
                         const fmi3ValueReference valueReferences[],
                         size_t nValueReferences,
                         const fmi3Clock values[]) {
    (void) instance; (void) valueReferences; (void) nValueReferences; (void) values;
    return fmi3Error;
}

/* ==================================================================== */
/* Informacao de dependencia entre variaveis (nao usada por este FMU)    */
/* ==================================================================== */

fmi3Status fmi3GetNumberOfVariableDependencies(fmi3Instance instance,
                                                fmi3ValueReference valueReference,
                                                size_t *nDependencies) {
    (void) instance; (void) valueReference;
    if (nDependencies) *nDependencies = 0;
    return fmi3OK;
}

fmi3Status fmi3GetVariableDependencies(fmi3Instance instance,
                                        fmi3ValueReference dependent,
                                        size_t elementIndicesOfDependent[],
                                        fmi3ValueReference independents[],
                                        size_t elementIndicesOfIndependents[],
                                        fmi3DependencyKind dependencyKinds[],
                                        size_t nDependencies) {
    (void) instance; (void) dependent; (void) elementIndicesOfDependent;
    (void) independents; (void) elementIndicesOfIndependents;
    (void) dependencyKinds; (void) nDependencies;
    return fmi3OK; /* nenhuma dependencia declarada (nDependencies e sempre 0) */
}

/* ==================================================================== */
/* Estado interno do FMU: get/set/serializacao — nao suportado           */
/* ==================================================================== */

fmi3Status fmi3GetFMUState(fmi3Instance instance, fmi3FMUState *FMUState) {
    (void) instance;
    if (FMUState) *FMUState = NULL;
    return fmi3Error;
}

fmi3Status fmi3SetFMUState(fmi3Instance instance, fmi3FMUState FMUState) {
    (void) instance; (void) FMUState;
    return fmi3Error;
}

fmi3Status fmi3FreeFMUState(fmi3Instance instance, fmi3FMUState *FMUState) {
    (void) instance;
    if (FMUState) *FMUState = NULL;
    return fmi3OK;
}

fmi3Status fmi3SerializedFMUStateSize(fmi3Instance instance,
                                       fmi3FMUState FMUState,
                                       size_t *size) {
    (void) instance; (void) FMUState;
    if (size) *size = 0;
    return fmi3Error;
}

fmi3Status fmi3SerializeFMUState(fmi3Instance instance,
                                  fmi3FMUState FMUState,
                                  fmi3Byte serializedState[],
                                  size_t size) {
    (void) instance; (void) FMUState; (void) serializedState; (void) size;
    return fmi3Error;
}

fmi3Status fmi3DeserializeFMUState(fmi3Instance instance,
                                    const fmi3Byte serializedState[],
                                    size_t size,
                                    fmi3FMUState *FMUState) {
    (void) instance; (void) serializedState; (void) size;
    if (FMUState) *FMUState = NULL;
    return fmi3Error;
}

/* ==================================================================== */
/* Derivadas parciais — nao suportado                                    */
/* ==================================================================== */

fmi3Status fmi3GetDirectionalDerivative(fmi3Instance instance,
                                         const fmi3ValueReference unknowns[],
                                         size_t nUnknowns,
                                         const fmi3ValueReference knowns[],
                                         size_t nKnowns,
                                         const fmi3Float64 seed[],
                                         size_t nSeed,
                                         fmi3Float64 sensitivity[],
                                         size_t nSensitivity) {
    (void) instance; (void) unknowns; (void) nUnknowns; (void) knowns;
    (void) nKnowns; (void) seed; (void) nSeed; (void) sensitivity; (void) nSensitivity;
    return fmi3Error;
}

fmi3Status fmi3GetAdjointDerivative(fmi3Instance instance,
                                     const fmi3ValueReference unknowns[],
                                     size_t nUnknowns,
                                     const fmi3ValueReference knowns[],
                                     size_t nKnowns,
                                     const fmi3Float64 seed[],
                                     size_t nSeed,
                                     fmi3Float64 sensitivity[],
                                     size_t nSensitivity) {
    (void) instance; (void) unknowns; (void) nUnknowns; (void) knowns;
    (void) nKnowns; (void) seed; (void) nSeed; (void) sensitivity; (void) nSensitivity;
    return fmi3Error;
}

/* ==================================================================== */
/* Modo de configuracao/reconfiguracao — sem parametros estruturais      */
/* ==================================================================== */

fmi3Status fmi3EnterConfigurationMode(fmi3Instance instance) {
    return instance ? fmi3OK : fmi3Error;
}

fmi3Status fmi3ExitConfigurationMode(fmi3Instance instance) {
    return instance ? fmi3OK : fmi3Error;
}

/* ==================================================================== */
/* Clocks — este modelo nao declara nenhum clock                         */
/* ==================================================================== */

fmi3Status fmi3GetIntervalDecimal(fmi3Instance instance,
                                   const fmi3ValueReference valueReferences[],
                                   size_t nValueReferences,
                                   fmi3Float64 intervals[],
                                   fmi3IntervalQualifier qualifiers[]) {
    (void) instance; (void) valueReferences; (void) nValueReferences;
    (void) intervals; (void) qualifiers;
    return fmi3Error;
}

fmi3Status fmi3GetIntervalFraction(fmi3Instance instance,
                                    const fmi3ValueReference valueReferences[],
                                    size_t nValueReferences,
                                    fmi3UInt64 counters[],
                                    fmi3UInt64 resolutions[],
                                    fmi3IntervalQualifier qualifiers[]) {
    (void) instance; (void) valueReferences; (void) nValueReferences;
    (void) counters; (void) resolutions; (void) qualifiers;
    return fmi3Error;
}

fmi3Status fmi3GetShiftDecimal(fmi3Instance instance,
                                const fmi3ValueReference valueReferences[],
                                size_t nValueReferences,
                                fmi3Float64 shifts[]) {
    (void) instance; (void) valueReferences; (void) nValueReferences; (void) shifts;
    return fmi3Error;
}

fmi3Status fmi3GetShiftFraction(fmi3Instance instance,
                                 const fmi3ValueReference valueReferences[],
                                 size_t nValueReferences,
                                 fmi3UInt64 counters[],
                                 fmi3UInt64 resolutions[]) {
    (void) instance; (void) valueReferences; (void) nValueReferences;
    (void) counters; (void) resolutions;
    return fmi3Error;
}

fmi3Status fmi3SetIntervalDecimal(fmi3Instance instance,
                                   const fmi3ValueReference valueReferences[],
                                   size_t nValueReferences,
                                   const fmi3Float64 intervals[]) {
    (void) instance; (void) valueReferences; (void) nValueReferences; (void) intervals;
    return fmi3Error;
}

fmi3Status fmi3SetIntervalFraction(fmi3Instance instance,
                                    const fmi3ValueReference valueReferences[],
                                    size_t nValueReferences,
                                    const fmi3UInt64 counters[],
                                    const fmi3UInt64 resolutions[]) {
    (void) instance; (void) valueReferences; (void) nValueReferences;
    (void) counters; (void) resolutions;
    return fmi3Error;
}

fmi3Status fmi3SetShiftDecimal(fmi3Instance instance,
                                const fmi3ValueReference valueReferences[],
                                size_t nValueReferences,
                                const fmi3Float64 shifts[]) {
    (void) instance; (void) valueReferences; (void) nValueReferences; (void) shifts;
    return fmi3Error;
}

fmi3Status fmi3SetShiftFraction(fmi3Instance instance,
                                 const fmi3ValueReference valueReferences[],
                                 size_t nValueReferences,
                                 const fmi3UInt64 counters[],
                                 const fmi3UInt64 resolutions[]) {
    (void) instance; (void) valueReferences; (void) nValueReferences;
    (void) counters; (void) resolutions;
    return fmi3Error;
}

fmi3Status fmi3EvaluateDiscreteStates(fmi3Instance instance) {
    return instance ? fmi3OK : fmi3Error;
}

fmi3Status fmi3UpdateDiscreteStates(fmi3Instance instance,
                                     fmi3Boolean *discreteStatesNeedUpdate,
                                     fmi3Boolean *terminateSimulation,
                                     fmi3Boolean *nominalsOfContinuousStatesChanged,
                                     fmi3Boolean *valuesOfContinuousStatesChanged,
                                     fmi3Boolean *nextEventTimeDefined,
                                     fmi3Float64 *nextEventTime) {
    (void) instance;
    if (discreteStatesNeedUpdate) *discreteStatesNeedUpdate = fmi3False;
    if (terminateSimulation) *terminateSimulation = fmi3False;
    if (nominalsOfContinuousStatesChanged) *nominalsOfContinuousStatesChanged = fmi3False;
    if (valuesOfContinuousStatesChanged) *valuesOfContinuousStatesChanged = fmi3False;
    if (nextEventTimeDefined) *nextEventTimeDefined = fmi3False;
    if (nextEventTime) *nextEventTime = 0.0;
    return fmi3OK;
}

/* ==================================================================== */
/* Funcoes de Model Exchange — nao suportadas (este FMU e so-CS)         */
/* ==================================================================== */

fmi3Status fmi3EnterContinuousTimeMode(fmi3Instance instance) {
    return instance ? fmi3Error : fmi3Error;
}

fmi3Status fmi3CompletedIntegratorStep(fmi3Instance instance,
                                        fmi3Boolean noSetFMUStatePriorToCurrentPoint,
                                        fmi3Boolean *enterEventMode,
                                        fmi3Boolean *terminateSimulation) {
    (void) instance; (void) noSetFMUStatePriorToCurrentPoint;
    if (enterEventMode) *enterEventMode = fmi3False;
    if (terminateSimulation) *terminateSimulation = fmi3False;
    return fmi3Error;
}

fmi3Status fmi3SetTime(fmi3Instance instance, fmi3Float64 time) {
    (void) instance; (void) time;
    return fmi3Error;
}

fmi3Status fmi3SetContinuousStates(fmi3Instance instance,
                                    const fmi3Float64 continuousStates[],
                                    size_t nContinuousStates) {
    (void) instance; (void) continuousStates; (void) nContinuousStates;
    return fmi3Error;
}

fmi3Status fmi3GetContinuousStateDerivatives(fmi3Instance instance,
                                              fmi3Float64 derivatives[],
                                              size_t nContinuousStates) {
    (void) instance; (void) derivatives; (void) nContinuousStates;
    return fmi3Error;
}

fmi3Status fmi3GetEventIndicators(fmi3Instance instance,
                                   fmi3Float64 eventIndicators[],
                                   size_t nEventIndicators) {
    (void) instance; (void) eventIndicators; (void) nEventIndicators;
    return fmi3Error;
}

fmi3Status fmi3GetContinuousStates(fmi3Instance instance,
                                    fmi3Float64 continuousStates[],
                                    size_t nContinuousStates) {
    (void) instance; (void) continuousStates; (void) nContinuousStates;
    return fmi3Error;
}

fmi3Status fmi3GetNominalsOfContinuousStates(fmi3Instance instance,
                                              fmi3Float64 nominals[],
                                              size_t nContinuousStates) {
    (void) instance; (void) nominals; (void) nContinuousStates;
    return fmi3Error;
}

fmi3Status fmi3GetNumberOfEventIndicators(fmi3Instance instance,
                                           size_t *nEventIndicators) {
    (void) instance;
    if (nEventIndicators) *nEventIndicators = 0;
    return fmi3OK;
}

fmi3Status fmi3GetNumberOfContinuousStates(fmi3Instance instance,
                                            size_t *nContinuousStates) {
    (void) instance;
    if (nContinuousStates) *nContinuousStates = 0; /* modo ME nao suportado */
    return fmi3OK;
}

/* ==================================================================== */
/* Funcoes de Co-Simulation — o coracao deste FMU                        */
/* ==================================================================== */

fmi3Status fmi3EnterStepMode(fmi3Instance instance) {
    return instance ? fmi3OK : fmi3Error;
}

fmi3Status fmi3GetOutputDerivatives(fmi3Instance instance,
                                     const fmi3ValueReference valueReferences[],
                                     size_t nValueReferences,
                                     const fmi3Int32 orders[],
                                     fmi3Float64 values[],
                                     size_t nValues) {
    (void) instance; (void) valueReferences; (void) nValueReferences;
    (void) orders; (void) values; (void) nValues;
    return fmi3Error; /* maxOutputDerivativeOrder = 0 no modelDescription.xml */
}

fmi3Status fmi3DoStep(fmi3Instance instance,
                       fmi3Float64 currentCommunicationPoint,
                       fmi3Float64 communicationStepSize,
                       fmi3Boolean noSetFMUStatePriorToCurrentPoint,
                       fmi3Boolean *eventHandlingNeeded,
                       fmi3Boolean *terminateSimulation,
                       fmi3Boolean *earlyReturn,
                       fmi3Float64 *lastSuccessfulTime) {
    (void) noSetFMUStatePriorToCurrentPoint;

    ModelInstance *m = (ModelInstance *) instance;
    if (!m) return fmi3Error;

    if (communicationStepSize < 0.0) return fmi3Error;

    if (communicationStepSize > 0.0) {
        /* Sub-divide o passo de comunicacao H em micro-passos <= MICRO_DT
         * para manter a precisao do RK4 independentemente de quao grosso
         * for o passo escolhido pelo mestre de co-simulacao. As entradas
         * u_volts/tau_load ficam mantidas (ZOH) por todo o intervalo H —
         * e exatamente essa retencao que gera o "erro de acoplamento"
         * discutido na Aula 8 quando H cresce. */
        long n_sub = (long) ceil(communicationStepSize / MICRO_DT);
        if (n_sub < 1) n_sub = 1;
        double h = communicationStepSize / (double) n_sub;

        for (long k = 0; k < n_sub; k++) {
            rk4_step(m, h);
        }
    }

    m->time = currentCommunicationPoint + communicationStepSize;

    if (eventHandlingNeeded) *eventHandlingNeeded = fmi3False;
    if (terminateSimulation) *terminateSimulation = fmi3False;
    if (earlyReturn) *earlyReturn = fmi3False;
    if (lastSuccessfulTime) *lastSuccessfulTime = m->time;

    return fmi3OK;
}

/* ==================================================================== */
/* Funcoes de Scheduled Execution — nao suportadas                       */
/* ==================================================================== */

fmi3Status fmi3ActivateModelPartition(fmi3Instance instance,
                                       fmi3ValueReference clockReference,
                                       fmi3Float64 activationTime) {
    (void) instance; (void) clockReference; (void) activationTime;
    return fmi3Error;
}
