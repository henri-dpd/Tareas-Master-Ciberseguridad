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

#### Consecuencias sobre la Salud Pública (Integridad)

La **manipulación de parámetros químicos** es la consecuencia más crítica.

- **Toxicidad:** Un aumento malintencionado en la dosificación de cloro o agentes correctores de pH podría provocar efectos adversos en la salud (especialmente en colectivos vulnerables) y obligaría a activar medidas de emergencia.
- **Insalubridad:** Por el contrario, si se reduce o se inhibe la desinfección, aumenta el riesgo de proliferación de patógenos (bacterias, virus) en la red de distribución, pudiendo derivar en brotes.

#### Consecuencias Operativas y Técnicas (Disponibilidad)

La **Denegación de Servicio (DoS)** o las **Fallas físicas críticas** afectan la continuidad:

- **Daños en Activos:** Una manipulación brusca de válvulas o una parada súbita de bombas puede provocar el fenómeno de _golpe de ariete_ y ocasionar daños en tuberías o equipos, aumentando el tiempo de recuperación.
- **Ceguera Operativa:** En el caso de ataques MitM, el operador podría estar tomando decisiones basadas en datos falsos, lo que retrasa la detección de desbordamientos o fugas críticas.

#### Consecuencias Socioeconómicas e Interdependencias

Dada la interconexión entre infraestructuras críticas descrita en el sector agua:

- **Impacto en Sanidad:** Hospitales y centros de salud en la Comunidad de Madrid verían comprometida su capacidad operativa (esterilización, higiene y tratamientos médicos).
- **Seguridad Ciudadana:** Una caída en la presión de la red anularía la efectividad de los sistemas de extinción de incendios (hidrantes).
- **Impacto Económico:** Parada de la industria local y del sector servicios que dependen directamente del suministro constante de agua tratada.

#### Consecuencias Ambientales

Además del impacto en personas y servicio, en una ETAP también puede haber **impacto ambiental**, sobre todo si el incidente deriva en vertidos, consumos anómalos o tratamiento fuera de especificación:

- **Vertidos o alivios no controlados:** una parada súbita, una avería (p. ej., por golpe de ariete) o una mala maniobra puede acabar en alivios/derivaciones de agua sin el tratamiento previsto, con afectación potencial de cauces, suelos o ecosistemas cercanos.
- **Sobredosificación de reactivos:** una manipulación de dosificación puede incrementar la carga química en el proceso y generar efluentes o lodos con peores características, complicando su gestión.
- **Consumo energético y emisiones indirectas:** operar en modo degradado (grupos electrógenos) o con ineficiencias por fallos de control puede aumentar consumos y, por extensión, la huella asociada.
- **Mayor generación de residuos/lodos:** un mal control del proceso (coagulación/floculación/filtración) puede elevar la cantidad de lodos y residuos que hay que tratar y transportar.

#### Consecuencias Legales y Reputacionales

- **Sanciones y medidas regulatorias:** Un incidente grave podría implicar incumplimientos de obligaciones de seguridad (Ley PIC y marcos como NIS2, según aplique), con potenciales sanciones, requerimientos correctivos y auditorías.
- **Alarma Social:** La pérdida de confianza en un suministro tan básico como el agua puede generar alarma social y presión mediática, complicando la gestión del incidente.

### 1.4 Medidas de mitigación para los riesgos identificados

En una ETAP, identificar riesgos está bien, pero lo importante es **cómo los reduces sin romper la operación**. En OT manda el binomio: que el servicio siga funcionando y que el proceso sea seguro.

Teniendo en mira los riesgos más altos (V=6), hay tres prioridades claras:

- **Evitar accesos no autorizados** a sistemas de operación (porque habilita el resto).
- **Impedir la manipulación peligrosa de setpoints** (integridad del tratamiento) incluso aunque alguien “consiga entrar”.
- **Mantener capacidad de control en modo degradado** si cae la supervisión (DoS/indisponibilidad OT/SCADA).

#### Gobernanza y operación

Aquí busco que la planta sea **auditable y controlable** en el día a día (especialmente cuando hay terceros y mantenimiento).

- **Inventario y criticidad de activos OT:** PLCs, SCADA/HMI, estación de ingeniería, enlaces, instrumentación y puntos de mando; qué depende de qué y qué duele más perder.
- **Gestión del cambio (MOC):** cambios en dosificación (cloro, pH, coagulantes) y en lógica de PLC se registran, se justifican y se revisan (si es viable, con doble validación: operación + responsable técnico).
- **Trazabilidad y cuentas nominativas:** evitar cuentas compartidas, registrar acciones relevantes y revisar periódicamente accesos (especialmente los de mantenimiento/contratas).

#### Arquitectura IT/OT y segmentación

La idea es que un incidente en IT no salte a OT, y que el acceso a equipos críticos pase por puntos controlados.

- **Separación IT–OT real:** la red corporativa y el acceso a Internet no deben tener ruta directa a PLC/SCADA; se usan **firewalls industriales** y reglas mínimas.
- **DMZ industrial y salto controlado:** para accesos remotos y transferencia de ficheros, usar una **DMZ** y un **jump server** (bastión). Así se controla y audita el acceso sin “abrir” la planta.
- **Mitigación de DoS/tormentas de red:** limitar y filtrar tráfico industrial, evitar “todo habla con todo”, y asegurar que existe operación local si la supervisión central se degrada.

#### Control de acceso y hardening

Una vez segmentado, el siguiente paso es endurecer el “quién entra” y el “desde dónde”, sin perder trazabilidad.

- **MFA para acceso remoto y de administración:** obligatorio para terceros y personal con privilegios, con ventanas de acceso y autorización explícita.
- **Mínimo privilegio y separación de funciones:** perfiles diferenciados (operación, mantenimiento, ingeniería) para reducir abuso de credenciales.
- **Endurecimiento de estaciones OT:** control de USB, deshabilitar servicios innecesarios, y parcheo coordinado con operación (en OT no se parchea “cuando salga”, se planifica).

#### Integridad del proceso

Esta parte es clave en agua: aunque el atacante tenga acceso a SCADA, el proceso debe tener **topes y lógica de seguridad** que le pongan freno.

- **Límites e interbloqueos en PLC (no solo en SCADA):** topes máximos/mínimos de setpoints, validaciones de rango y lógica de failsafe para impedir sobredosificación o maniobras peligrosas.
- **Alarmas por desviación y verificación operativa:** si la telemetría es incoherente (posible spoofing/fallo), el operador tiene procedimientos para confirmar (p. ej., muestreo/laboratorio) antes de aplicar cambios agresivos.
- **Versionado de setpoints/recetas y rollback:** historial de cambios y posibilidad de volver rápido a una configuración conocida y segura.

#### Monitorización y detección

Asumo que algo puede fallar o colarse; por eso necesito visibilidad y alertas que ayuden al operador a decidir.

- **IDS/monitorización industrial:** detección de patrones anómalos (escaneos, escritura inusual a PLC, cambios inesperados) y alertas útiles para MitM/Spoofing.
- **Centralización mínima de logs y sincronización horaria:** logs de SCADA/bastión/firewall y hora consistente para que la investigación posterior sea posible.
- **Validación cruzada de instrumentación:** comparar sensores y tendencias del proceso para detectar lecturas “imposibles” (fallo o manipulación).

#### Resiliencia y continuidad

Cuando el problema no se puede evitar (corte eléctrico, avería, ataque), la pregunta es: ¿cómo sigo operando y cómo recupero rápido?

- **Continuidad eléctrica probada:** SAI + grupos electrógenos con pruebas periódicas y procedimientos claros.
- **Mantenimiento preventivo y repuestos críticos:** reduce la probabilidad alta de fallos físicos y acelera recuperación.
- **Backups OT y recuperación:** copias de configuraciones SCADA/estación de ingeniería y programas de PLC, almacenadas de forma segura y con restauraciones probadas.
- **Stock crítico de reactivos (realista):** reserva considerando rotación/caducidad, más acuerdos con proveedores para reposición prioritaria.
- **Planes y simulacros:** operación manual, respuesta a incidentes y coordinación ante sequía/eventos extremos (si no se entrena, el plan no funciona).

| Amenaza de mi lista          | Medidas de mitigación (principal/es)                                                                   |
| :--------------------------- | :----------------------------------------------------------------------------------------------------- |
| **Acceso no autorizado**     | MFA, mínimo privilegio, cuentas nominativas, auditoría; acceso remoto vía DMZ/jump server.             |
| **Manipulación química**     | Límites/interbloqueos en PLC, MOC, versionado y rollback de setpoints/recetas, alarmas por desviación. |
| **Ataque DoS / Infecciones** | Segmentación IT/OT, filtrado y reglas mínimas, reducción de “todo a todo”, operación local degradada.  |
| **Ataque MitM / Spoofing**   | IDS industrial, logs y sincronía horaria, validación cruzada y verificación operativa (muestreo/lab).  |
| **Fallas en sensores**       | Validación cruzada, calibración/mantenimiento y alarmas conservadoras con confirmación manual.         |
| **Corte de luz / Averías**   | SAI+grupos con pruebas, mantenimiento preventivo, repuestos críticos y plan de recuperación.           |
| **Falta de reactivos**       | Stock crítico con control de caducidad y acuerdos de reposición prioritaria.                           |
| **Desastres / Sequía**       | Planes de contingencia, operación manual, coordinación y protocolos de emergencia/gestión de demanda.  |

### 1.5 Diseño y Configuración del Escenario de Red (Simulación)

Para la demostración técnica, he diseñado un laboratorio que simula (de forma simplificada) el segmento de control **OT** de la ETAP de Colmenar Viejo. Siguiendo los requisitos de la tarea, uso direccionamiento privado de **Clase B** dentro del rango **172.16.0.0/12**.

**Cálculo de red (según el enunciado):**
Sea $X$ el resultado de aplicar el módulo a los **últimos 3 dígitos del DNI**.

- **Fórmula:** $X = (\text{últimos 3 dígitos}) \pmod{255}$
- **Mi valor:** últimos 3 dígitos = **462** → $X = 462 \bmod 255 = 207$

Con esto, la red de trabajo queda:

- **Red OT simulada:** `172.16.207.0/24`
- **Máscara:** `255.255.255.0` (254 hosts útiles)
- **Puerta de enlace:** no es necesaria si todo el laboratorio está en la misma LAN (si se usa NAT/Internet en la VM, se configura aparte)

#### Esquema Gráfico de Red

El siguiente esquema representa la topología en estrella utilizada en el simulador:

- **Maestro (SCADA/HMI):** Estación de supervisión que consulta el estado de la planta.
- **Esclavo (ModbusPal):** Simulador de PLC industrial que gestiona los actuadores y sensores de la ETAP.
- **Atacante (Kali Linux):** Máquina de auditoría desde la que se inyectará el tráfico Modbus malicioso.

![Simulacion Ataque](Simulacion-Ataque.drawio.png)

#### Direccionamiento IP y Software

| Dispositivo  | Función           | Dirección IP     | Software / Herramientas  |
| :----------- | :---------------- | :--------------- | :----------------------- |
| **Maestro**  | Supervisión SCADA | `172.16.207.20`  | QModMaster / ScadaBR     |
| **Esclavo**  | PLC Dosificación  | `172.16.207.10`  | ModbusPal (Java)         |
| **Atacante** | Estación Kali     | `172.16.207.100` | Mbtget, Metasploit, Nmap |

Notas de direccionamiento:

- Reservo `172.16.207.20` para el rol de **maestro (SCADA/HMI)**, `172.16.207.10` para el **esclavo (PLC/ModbusPal)** y `172.16.207.100` para auditoría.
- La segmentación se deja plana a propósito para la práctica; en una ETAP real lo normal es que el atacante **no** esté en la misma LAN OT sin una intrusión previa (o un acceso físico).

#### Configuración del Mapa de Memoria (ModbusPal)

Se ha configurado el esclavo (Unit ID: 1) con los siguientes registros para representar el proceso de potabilización:

**12 Coils (Salidas Digitales - On/Off):**

1.  **Coil 1-2:** Bombas de captación de agua bruta (Embalse).
2.  **Coil 3-6:** Bombas de impulsión a alta presión (Salida a red).
3.  **Coil 7-10:** Válvulas de limpieza de filtros.
4.  **Coil 11-12:** Agitadores de mezcla de reactivos químicos.

**14 Holding Registers (Valores de 16 bits):**

- **40001:** Concentración de Cloro Residual (mg/L x100).
- **40002:** Nivel de pH (Acidez del agua).
- **40003:** Turbidez (NTU).
- **40004:** Caudal de entrada ($m^3/h$).
- **40005:** Caudal de salida ($m^3/h$).
- **40006:** Nivel Tanque Cloro (%).
- **40007:** Nivel Tanque Coagulante (%).
- **40008:** Presión tubería principal (Bar).
- **40009:** Conductividad.
- **40010:** Temperatura del agua.
- **40011-40014:** _Setpoints_ de seguridad (Límites programados por el operario).

#### Configuración de Comunicación

El Maestro está configurado para realizar consultas cíclicas (polling) cada 1000 ms al Esclavo (Unit ID: 1) en el puerto estándar **TCP/502**.

![Simulación](Simulacion.png)

En el laboratorio asumo que el atacante ya tiene presencia en la misma red `172.16.207.0/24` (misma LAN L2), lo que le permite observar e interactuar con el tráfico Modbus. En un escenario real, esto normalmente sería consecuencia de una fase previa (compromiso de IT con salto a OT, mala segmentación, o acceso físico a la red).

### 1.6 Simulación ataque Sistemas SCADA/ICS: Lectura de Registros/Coils

En esta fase, el objetivo es demostrar la **falta de confidencialidad** y de **control de acceso** en **Modbus TCP**, validando que un atacante en la misma LAN OT puede **leer** el estado del proceso (registros analógicos y coils digitales) sin credenciales.

- **Atacante:** Kali Linux `172.16.207.100`.
- **Maestro (SCADA/HMI):** `172.16.207.20`.
- **Esclavo (PLC simulado / ModbusPal):** `172.16.207.10` (Unit ID: 1, puerto TCP/502).
- **Alcance (lectura):** **Holding Registers** (14 registros, equivalentes a `40001–40014`) y **Coils** (12 coils, equivalentes a `00001–00012`) según el mapa definido en 1.5.

#### Observación de tráfico con Wireshark (sniffing)

Antes de lanzar consultas activas, capturé tráfico para confirmar:

- Dispositivos que hablan Modbus (`172.16.207.20` ↔ `172.16.207.10`).
- Uso del puerto **TCP/502**.
- Funciones en claro (p. ej., **0x03 Read Holding Registers**, **0x01 Read Coils**).

Esto es relevante porque Modbus TCP no cifra ni autentica: el contenido del proceso y las operaciones quedan visibles para cualquiera con acceso a la red.

![Auditoría Wireshark](Auditoria-Wireshark-Simulacion.png)

#### Lectura de Holding Registers con Metasploit

Con la información anterior, leí los **Holding Registers** del PLC simulado (valores de proceso como cloro, pH, caudales, etc., según el mapa de memoria del 1.5).

Comandos ejecutados en Metasploit:

```bash
use auxiliary/scanner/scada/modbusclient
set RHOSTS 172.16.207.10
set ACTION READ_HOLDING_REGISTERS
set DATA_ADDRESS 0
set NUMBER 14
set UNIT_NUMBER 1
run
```

La salida confirma que el atacante obtiene valores del proceso (p. ej., `1200`, `150`, `710`...), lo que supone **fuga de información operativa**.

![Auditoría Metasploit - Lectura de Registros](Auditoria-Leer-Registros-Simulacion.png)

#### Lectura de Coils con Metasploit

Después repetí el procedimiento para leer el estado digital (On/Off) de bombas, válvulas y actuadores representados por coils.

Comandos ejecutados en Metasploit:

```bash
set ACTION READ_COILS
set DATA_ADDRESS 0
set NUMBER 12
run
```

El PLC devuelve una cadena de bits (0/1) que refleja el estado operativo de los equipos.

![Auditoría Metasploit - Lectura de Coils](Auditoria-Leer-Coils-Simulacion.png)

#### Vulnerabilidad explotada y relación con el análisis de riesgos

La causa raíz es la **ausencia de seguridad por diseño** en Modbus TCP:

- **Sin autenticación/autorización:** conocer IP, Unit ID y puerto es suficiente para leer memoria.
- **Tráfico en texto claro:** facilita el descubrimiento de funciones, direcciones y valores.
- **Confianza implícita en la red OT:** el protocolo asume que “quien llega a la red” es legítimo.

Este ejercicio se alinea con los riesgos descritos en 1.2 (pérdida/engaño de monitorización y acceso no autorizado): si se puede leer el estado del proceso, es más fácil preparar ataques posteriores (p. ej., manipulación de setpoints o cambios de estado).

Las **medidas de mitigación** asociadas a este ataque se detallan en el apartado **1.8**.

### 1.7 Simulación ataque Sistemas SCADA/ICS: Modificación de Registros/Coils

En esta fase paso de la observación a la **manipulación activa del proceso**, demostrando el impacto sobre **Integridad**: un atacante en la misma LAN OT puede **escribir** valores en registros y coils sin autenticación.

- **Atacante:** Kali Linux `172.16.207.100`.
- **Maestro (SCADA/HMI):** `172.16.207.20`.
- **Esclavo (PLC simulado / ModbusPal):** `172.16.207.10` (Unit ID: 1, puerto TCP/502).

#### Escritura de Holding Registers (alteración de variables de proceso)

Partiendo del estado normal del proceso en el simulador (valores estables y coherentes), fuerzo cambios bruscos escribiendo directamente en memoria.

Estado inicial (antes del ataque):

![Registros antes de Ataque](Registros-Antes-Ataque-Simulacion.png)

Ejecución del ataque (Metasploit). Se usa `modbusclient` para sobreescribir valores en las direcciones de memoria definidas en el PLC simulado:

Comandos ejecutados:

```bash
use auxiliary/scanner/scada/modbusclient
set RHOSTS 172.16.207.10
set UNIT_NUMBER 1
set ACTION WRITE_REGISTER
set DATA_ADDRESS 2
set DATA 1400
run
set DATA_ADDRESS 0
set DATA 0
run
```

Evidencia de ejecución:

![Ataque - Escribir Registros](Auditoria-Escribir-Registros-Simulacion.png)

Resultado (después del ataque):

![Registros despues de ataque](Registros-Despues-Ataque-Simulacion.png)

#### Escritura de Coils (control de actuadores)

Además de variables analógicas, un atacante puede actuar sobre salidas digitales (coils), afectando a actuadores (bombas/válvulas) y forzando estados no deseados.

Estado inicial (antes del ataque):

![Coils antes de Ataque](Coils-Antes-Ataque-Simulacion.png)

Ejecución del ataque (Metasploit). Mantengo la sesión del módulo y cambio la acción a escritura de coils:

Comandos ejecutados:

```bash
set ACTION WRITE_COIL
set DATA_ADDRESS 1
set DATA 0
run
set DATA_ADDRESS 2
set DATA 0
run
```

Evidencia de ejecución:

![Ataque - Escribir Coils](Auditoria-Escribir-Coils-Simulacion.png)

Resultado (después del ataque):

![Coils despues de Ataque](Coils-Despues-Ataque-Simulacion.png)

#### Vulnerabilidad explotada y relación con el análisis de riesgos

La causa raíz es la **ausencia de seguridad por diseño en Modbus TCP**:

- **Falta de autenticación y autorización:** el PLC acepta escrituras sin verificar el origen.
- **Sin control de integridad/antireplay:** no hay mecanismo criptográfico que impida modificaciones.
- **Confianza implícita en la red OT:** el protocolo asume que todo nodo en la LAN es legítimo.

Este ataque valida el riesgo de **manipulación de parámetros de tratamiento (Integridad)** y **control de actuadores (Disponibilidad/seguridad del proceso)**, que en el análisis 1.2 se considera de impacto alto.

Las **medidas de mitigación** asociadas a este ataque se detallan en el apartado **1.8**.

### 1.8 Medidas de mitigación (continuación y detalle técnico)

Las pruebas realizadas en 1.6 (lectura) y 1.7 (escritura) evidencian que **Modbus TCP carece de autenticación, cifrado e integridad por diseño**. Por ello, la mitigación debe aplicarse como **Defensa en Profundidad**, combinando controles de red, de acceso y de lógica de proceso (alineado con 1.4).

#### Objetivo de mitigación

- Evitar que un equipo no autorizado alcance el segmento PLC (reducción de superficie y exposición).
- Impedir o limitar operaciones **WRITE** hacia PLCs (protección de integridad del proceso).
- Detectar de forma temprana lecturas/escrituras anómalas (capacidad de respuesta).

#### Controles a nivel de red (IT/OT)

- **Segmentación en zonas y conduits:** VLAN/segmentos separados para SCADA/PLC; sin rutas directas desde redes de usuario o Wi‑Fi hacia TCP/502.
- **Firewall industrial con reglas mínimas:** permitir solo los flujos necesarios (por IP/origen/destino/puerto) hacia `172.16.207.10:502`.
- **Filtrado por función (DPI) si está disponible:** reglas específicas para Modbus (p. ej., permitir `READ` desde el SCADA `172.16.207.20` y restringir `WRITE` a estaciones autorizadas y ventanas controladas).
- **Controles de Capa 2:** port-security / deshabilitar puertos no usados para reducir el riesgo de conexión física de un atacante a la LAN de control.

#### Controles de acceso y operación (personas/terceros)

- **Acceso remoto mediante DMZ/jump server + MFA:** el acceso a OT se realiza por salto controlado, con trazabilidad y aprobación.
- **Cuentas nominativas y mínimo privilegio:** separar perfiles (operación vs. ingeniería) y revisar accesos periódicamente.
- **Gestión del cambio (MOC):** cambios en lógica de PLC, recetas o setpoints con registro, justificación y validación.

#### Controles en PLC / lógica de proceso (integridad)

- **Validación de rangos e interbloqueos en PLC:** rechazar valores fuera de límites físicos (p. ej., pH extremo) y forzar estado seguro/alarma ante entradas incoherentes.
- **Hardening del dispositivo:** deshabilitar servicios de administración innecesarios y restringir interfaces de programación a hosts autorizados.
- **Seguridad de canal cuando sea viable:** usar el estándar **Modbus Security** (TLS con certificados) o, alternativamente, túneles cifrados en el conduit (siempre que sea compatible con latencia/operación).

#### Monitorización y detección temprana

- **IDS/monitorización industrial:** alertar ante patrones anómalos (p. ej., aparición de `WRITE_REGISTER`/`WRITE_COIL` desde hosts no esperados o lecturas masivas).
- **Centralización de logs y sincronización horaria:** NTP consistente y logs de firewall/jump server/SCADA para poder reconstruir el incidente.

#### Resumen de controles por ataque

| Ataque / Amenaza | Medida de mitigación técnica | Objetivo principal |
| :--- | :--- | :--- |
| **Sniffing (1.6)** | Segmentación + cifrado de canal (Modbus Security/TLS o túnel en conduit cuando aplique). | **Confidencialidad** |
| **Lectura no autorizada (1.6)** | ACL/firewall industrial (permitir solo SCADA autorizado) + control de acceso a OT (DMZ/jump). | **Autorización** |
| **Escritura de registros (1.7)** | DPI para bloquear `WRITE` + validación de rangos/interbloqueos en PLC. | **Integridad** |
| **Manipulación de coils (1.7)** | Restringir `WRITE_COIL` por origen/función + cuentas/roles y trazabilidad de cambios. | **Integridad/Disponibilidad** |

**Conclusión:** en una ETAP, la mitigación efectiva no “arregla Modbus”, sino que reduce exposición (segmentación), controla quién puede operar (acceso) y evita que valores peligrosos lleguen a tener efecto (interbloqueos/validaciones), con detección temprana para contener.