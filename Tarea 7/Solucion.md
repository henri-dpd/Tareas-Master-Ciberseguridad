# Introducción a las Infraestructuras Críticas

## 1. Introducción y Selección de la Infraestructura

Para esta tarea he elegido como infraestructura crítica el **Canal de Isabel II**, centrándome en la **Estación de Tratamiento de Agua Potable (ETAP) de Colmenar Viejo** (Comunidad de Madrid).

El Canal de Isabel II se considera un **Operador Crítico** bajo el marco de la **Ley 8/2011 (Ley PIC)**, ya que el suministro de agua es un servicio esencial para la salud pública y el funcionamiento normal de la sociedad. En concreto, una ETAP es un buen caso de estudio porque combina operación física (bombas, válvulas, reactivos) con sistemas **OT/SCADA/PLC**; un incidente en esa parte de control podría tener un impacto muy relevante en la población.

### 1.1 Marco de Trabajo y Criterio de Evaluación

Para no hacerlo excesivamente complejo, he aplicado un análisis simplificado inspirado en **MAGERIT** y en el **NIST Risk Management Framework (RMF)**, usando **NIST SP 800-30** como guía práctica para estimar probabilidad e impacto. La métrica elegida es la típica: **Riesgo = Probabilidad (P) x Impacto (I)**.

- **Probabilidad (P):** (1: Baja, 2: Media, 3: Alta).
- **Impacto (I):** (1: Bajo, 2: Grave, 3: Muy Grave).
- **Valoración Final (V):**
  - **1 - 2:** Riesgo Bajo.
  - **3 - 4:** Riesgo Medio.
  - **6 - 9:** Riesgo Alto / Crítico.

### 1.2 Identificación y Evaluación de Amenazas

En este punto he intentado ser muy directo: primero pienso en los **activos/servicios** de la ETAP y, a partir de ahí, saco amenazas realistas. El análisis es **simplificado** y se apoya en dos marcos:

- **MAGERIT (activos → amenazas → impacto):** identificación de activos/servicios esenciales en una ETAP (proceso de potabilización, red OT/SCADA/PLC, instrumentación y sensores, comunicaciones, energía, reactivos químicos, personal y procedimientos) y listado de amenazas que afectan a **Integridad** y **Disponibilidad** principalmente.
- **NIST Risk Management Framework (RMF):**
  - **CATEGORIZE:** por el tipo de infraestructura (abastecimiento de agua), el impacto base se considera **alto** en **Integridad** (calidad del agua) y **Disponibilidad** (continuidad del suministro) por su relación directa con salud pública.
  - **ASSESS:** se estima **Probabilidad (P)** e **Impacto (I)** por amenaza y se calcula la **Valoración (V)** con $V = P \times I$.

**Criterio de evaluación usado (P e I):**

- **Probabilidad (P):**
  - **1 (Baja):** escenario poco frecuente o bien mitigado por controles/alternativas.
  - **2 (Media):** escenario factible (p. ej., acceso a red OT/credenciales, dependencias operativas habituales).
  - **3 (Alta):** escenario probable por exposición elevada o por desgaste/criticidad de activos físicos.
- **Impacto (I):**
  - **1 (Bajo):** afectación local, recuperable, sin comprometer calidad global ni continuidad.
  - **2 (Grave):** degradación relevante del servicio, pérdida de visibilidad/operación o incumplimiento acotado.
  - **3 (Muy grave):** agua fuera de especificación o interrupción significativa del suministro; impacto sistémico (salud, regulatorio, reputacional).

**Listado simple de amenazas (con criterio por caso):**

| Amenaza (Dimensión)                                                | Escenario y criterio de identificación                                                                                                                    | Criterio aplicado (P/I)                                                                                                                                                                          |  P  |  I  |  Valoración   |
| :----------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: | :-: | :-----------: |
| **Manipulación de parámetros de tratamiento (Integridad)**         | Alteración de _setpoints_ (cloración, coagulación, pH) desde SCADA/estación de ingeniería o cambios no autorizados en PLC.                                | **P=2** si se obtiene acceso a red OT/credenciales (operación o mantenimiento). **I=3** por riesgo de agua no potable y efecto directo en salud pública.                                         |  2  |  3  | **6 (Alto)**  |
| **Denegación de servicio en red OT/SCADA (Disponibilidad)**        | Saturación/bloqueo de comunicaciones OT o indisponibilidad del SCADA/HMI que impide operar bombeo y proceso.                                              | **P=2** por dependencia de comunicaciones y protocolos industriales. **I=3** por posible parada del proceso o incapacidad de control en tiempo real.                                             |  2  |  3  | **6 (Alto)**  |
| **Acceso no autorizado a sistemas de operación (C/I/D)**           | Robo/abuso de credenciales (operadores/contratistas), acceso remoto de soporte o abuso de privilegios en estación de ingeniería/SCADA.                    | **P=2** por dependencia habitual de cuentas privilegiadas y terceros. **I=3** porque habilita cambios persistentes que afectan integridad y disponibilidad.                                      |  2  |  3  | **6 (Alto)**  |
| **Pérdida/engaño de monitorización (MitM/Spoofing) (Integridad)**  | Intercepción o suplantación de telemetría: el operador visualiza valores falsos (caudales, cloro residual, turbidez) y decide con información incorrecta. | **P=2** si existe punto de acceso a red OT y tráfico sin autenticación/validación fuerte. **I=2** por degradación operativa relevante, normalmente con verificaciones adicionales y muestreos.   |  2  |  2  | **4 (Medio)** |
| **Pérdida de comunicaciones críticas (Disponibilidad)**            | Caída de enlaces (fibra/radio) entre zonas del proceso o con centro de control, degradando operación y tiempos de respuesta.                              | **P=2** por fallos puntuales plausibles en enlaces críticos. **I=2** por pérdida de visibilidad/operación remota y aumento del riesgo operacional (con procedimientos manuales de contingencia). |  2  |  2  | **4 (Medio)** |
| **Fallas físicas o averías críticas (Disponibilidad)**             | Rotura/degradación de bombas, válvulas, filtros o cuadros eléctricos por fatiga, corrosión o mantenimiento insuficiente.                                  | **P=3** por probabilidad inherente a activos físicos en operación continua. **I=2** por reducción de capacidad y posibles paradas parciales (suele haber redundancia parcial).                   |  3  |  2  | **6 (Alto)**  |
| **Interrupción del suministro eléctrico externo (Disponibilidad)** | Caída de red eléctrica; operación en modo degradado con SAI/grupos hasta restablecimiento.                                                                | **P=1** por menor frecuencia relativa y existencia de continuidad eléctrica. **I=3** porque un fallo prolongado o insuficiencia del respaldo puede detener el proceso.                           |  1  |  3  | **3 (Medio)** |
| **Desastres naturales / fenómenos climáticos (Disponibilidad)**    | Inundaciones/tormentas/olas de calor con daños físicos, cortes de acceso o afectación de infraestructuras auxiliares.                                     | **P=1** por menor frecuencia (eventos extremos). **I=2** por impacto operativo relevante y tiempos de recuperación no inmediatos.                                                                |  1  |  2  | **2 (Bajo)**  |
| **Falla en la cadena de suministro de reactivos (Disponibilidad)** | Escasez/retardo de reactivos (cloro, coagulantes) o incidentes logísticos que limitan el tratamiento.                                                     | **P=1** por contratos y stock de seguridad habituales. **I=3** porque sin reactivos críticos la potabilización se reduce drásticamente o se detiene.                                             |  1  |  3  | **3 (Medio)** |
| **Fallas en sensores de calidad e instrumentación (Integridad)**   | Lecturas erróneas o pérdida de calibración en sensores (turbidez, cloro residual, pH), afectando control automático y decisiones.                         | **P=2** por deriva/calibración y fallos relativamente comunes. **I=2** por riesgo de tratamiento inadecuado y necesidad de operación manual, normalmente con validaciones cruzadas.              |  2  |  2  | **4 (Medio)** |
| **Sequía prolongada (Disponibilidad)**                             | Reducción de agua bruta disponible en el sistema de embalses/cuencas que abastecen la red, afectando caudal y continuidad global.                         | **P=2** por recurrencia creciente de episodios de sequía. **I=1** a nivel de ETAP (la gestión se realiza principalmente a nivel de red/sistema y demanda).                                       |  2  |  1  | **2 (Bajo)**  |

**Valoración final del riesgo identificado (resumen):**

- **Riesgo Alto/Crítico (V=6):**
  - **Manipulación de parámetros de tratamiento (I):** aunque no sea el evento más frecuente, cuando ocurre el impacto es máximo por afectar directamente a la **calidad del agua**.
  - **Denegación de servicio OT/SCADA (D):** la indisponibilidad de supervisión/control puede llevar a parada del proceso o a operación insegura en poco tiempo.
  - **Acceso no autorizado a sistemas de operación (C/I/D):** funciona como _amenaza habilitadora_ (permite encadenar cambios y persistencia), por lo que eleva el riesgo real del conjunto.
  - **Fallas físicas/averías críticas (D):** en una ETAP hay activos físicos en operación continua; la probabilidad es alta y el impacto operativo es relevante aunque exista cierta redundancia.

- **Riesgo Medio (V=3–4):** MitM/engaño de monitorización, pérdida de comunicaciones, fallos de instrumentación/sensores e interrupción eléctrica o falta de reactivos (en estos dos últimos casos, **I** es alto pero **P** es menor por medidas habituales de continuidad y stock).

- **Riesgo Bajo (V=2):** eventos climáticos extremos y sequía (en este análisis se valoran como menor probabilidad o con impacto gestionado principalmente a nivel de sistema/red).

**Conclusión:** en una ETAP el riesgo queda dominado por escenarios que afectan a **Integridad del proceso** y **Disponibilidad operativa** en el entorno **OT**, porque combinan (1) impacto inmediato sobre población y cumplimiento, (2) ventanas de detección/contención cortas y (3) dependencia de sistemas de control y de activos físicos.

### 1.3 Posibles consecuencias de los riesgos identificados

La materialización de las amenazas con mayor valoración de riesgo (Nivel 6) en la ETAP de Colmenar Viejo acarrearía consecuencias en múltiples dimensiones, dada la naturaleza de servicio esencial del Canal de Isabel II:

#### A. Consecuencias sobre la Salud Pública (Integridad)

La **manipulación de parámetros químicos** es la consecuencia más crítica.

- **Toxicidad:** Un aumento malintencionado en la dosificación de cloro o agentes correctores de pH podría provocar efectos adversos en la salud (especialmente en colectivos vulnerables) y obligaría a activar medidas de emergencia.
- **Insalubridad:** Por el contrario, si se reduce o se inhibe la desinfección, aumenta el riesgo de proliferación de patógenos (bacterias, virus) en la red de distribución, pudiendo derivar en brotes.

#### B. Consecuencias Operativas y Técnicas (Disponibilidad)

La **Denegación de Servicio (DoS)** o las **Fallas físicas críticas** afectan la continuidad:

- **Daños en Activos:** Una manipulación brusca de válvulas o una parada súbita de bombas puede provocar el fenómeno de _golpe de ariete_ y ocasionar daños en tuberías o equipos, aumentando el tiempo de recuperación.
- **Ceguera Operativa:** En el caso de ataques MitM, el operador podría estar tomando decisiones basadas en datos falsos, lo que retrasa la detección de desbordamientos o fugas críticas.

#### C. Consecuencias Socioeconómicas e Interdependencias

Dada la interconexión entre infraestructuras críticas descrita en el sector agua:

- **Impacto en Sanidad:** Hospitales y centros de salud en la Comunidad de Madrid verían comprometida su capacidad operativa (esterilización, higiene y tratamientos médicos).
- **Seguridad Ciudadana:** Una caída en la presión de la red anularía la efectividad de los sistemas de extinción de incendios (hidrantes).
- **Impacto Económico:** Parada de la industria local y del sector servicios que dependen directamente del suministro constante de agua tratada.

#### D. Consecuencias Legales y Reputacionales

- **Sanciones y medidas regulatorias:** Un incidente grave podría implicar incumplimientos de obligaciones de seguridad (Ley PIC y marcos como NIS2, según aplique), con potenciales sanciones, requerimientos correctivos y auditorías.
- **Alarma Social:** La pérdida de confianza en un suministro tan básico como el agua puede generar alarma social y presión mediática, complicando la gestión del incidente.
