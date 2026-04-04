# Introducción a la respuesta a incidentes

## 1. Tarea 1

### 1.1 Errores cometidos en las primeras horas

**Falta de procedimientos y desorganización**: El error principal es no tener un plan de respuesta por escrito. Esto generó una respuesta nula o inefectiva, ya que no se definieron roles ni pasos a seguir según el tipo de incidente.

**Mala gestión técnica y pérdida de evidencia forense**: Se reiniciaron servidores y se apagaron equipos sin investigar la incidencia real ni extraer logs previamente. Reiniciar no va a descifrar los archivos y solo provoca la pérdida de datos volátiles fundamentales para el análisis forense ; lo ideal habría sido aplicar una cuarentena sin apagar las máquinas.

**Inexistencia de personal especializado**: No contar con personal dedicado en el CERT interno y retrasar el contacto con el proveedor de ciberseguridad fue crítico. Ellos son los que deben encargarse de contener e investigar para mitigar el impacto real.

**Gestión negligente de los backups**: Se intentó restaurar el backup sin revisar su estado, olvidando que las copias son el primer objetivo de los atacantes para evitar que la empresa mitigue el impacto. Además, restaurar directamente sin haber analizado antes los equipos afectados borra pruebas clave.

**Contacto directo con los atacantes sin autorización**: Un administrador contactó con el grupo criminal sin planificarlo con la directiva o el equipo legal. Esto no garantiza resolver el incidente ni recuperarse tras pagar, y expone a la empresa innecesariamente.

### 1.2. Clasificación del incidente

**Taxonomía**: Código Dañino (Malware) - Ransomware. Se identifica así porque el incidente consiste en el cifrado de archivos de red compartidos por un software malicioso llamado "DarkUCM". Además, existe una extorsión clara al exigir un pago de 2,5 BTC para recuperar el acceso.

**Peligrosidad**: Alta. Aunque aún no conocemos el alcance total, ya afecta a servicios críticos como los archivos compartidos de la red. El hecho de que el ransomware se haya reactivado y propagado a nuevas unidades tras reiniciar el servidor indica que la amenaza está activa y en expansión.

**Impacto**: Alto. Al ser una empresa financiera, la indisponibilidad de archivos compartidos bloquea la operativa de los empleados. El impacto es significativo por la naturaleza del sector (financiero) y porque ya se están viendo afectados procesos de negocio el lunes por la mañana, comprometiendo datos que pueden ser críticos.

### 1.3. Sesión de evaluación preliminar

Como Incident Handler, realizaría las siguientes 5 preguntas clave para tomar el control de la situación:

_¿Disponéis de un inventario actualizado de activos y cuáles de ellos están identificados como críticos para el negocio?_ Necesito saber qué máquinas son el "corazón" de la empresa (servidores de base de datos, controladores de dominio, etc.) para priorizar su protección y evaluar el alcance real del impacto en la operativa.¿
_Cuál es el esquema actual de segmentación de la red y qué dispositivos de seguridad (Firewalls, WAF, VPN) están activos?_
Esto ayuda a entender si existe aislamiento entre departamentos o si la red es plana. Es fundamental para diseñar medidas de contención inmediata y evitar que el ransomware siga saltando de una subred a otra.
_¿Qué herramientas de monitorización y respuesta tenéis (EDR, SIEM, Antivirus) y dónde se centralizan sus logs?_
Para el análisis forense y la detección activa, necesito saber si hay trazas de la ejecución del malware o de conexiones sospechosas. Saber dónde están los logs permite asegurar que no se sobrescriban o sean borrados por el atacante.
_¿Cuál es el estado y la ubicación de las copias de seguridad, y están aisladas de la red principal (offline/inmutables)?_
Antes de intentar cualquier recuperación, debemos asegurar que el backup no está cifrado ni comprometido. Si las copias están conectadas a la red infectada, podrían ser el próximo objetivo o ya estar inservibles.
_¿Qué acciones técnicas exactas se han ejecutado desde la detección del primer aviso hasta ahora?_
Necesito saber si se han reiniciado equipos o restaurado datos para valorar qué evidencia volátil (en RAM o logs) se ha podido perder ya. Esto evita que sigamos cometiendo errores que dificulten el análisis de la causa raíz.

### 1.4. Medidas iniciales de contención

Como no podemos cortar Internet totalmente, mi prioridad sería frenar el movimiento lateral y asegurar la supervivencia de las evidencias. Estas son las 5 medidas:

**Segmentación de emergencia y control de tráfico**: Al ser una red plana, el atacante se mueve sin restricciones. Implementaría reglas de firewall para bloquear puertos críticos (RDP, SMB) y crearía zonas de seguridad para aislar los servidores sanos de la red infectada.

**Extracción prioritaria de logs y evidencias volátiles**: Antes de que se sobrescriban o el atacante los borre, realizaría la recolección de logs de los Firewalls, Proxies y de los sistemas afectados. Me centraría especialmente en volcar la información de los equipos que siguen encendidos para no perder conexiones de red activas y procesos en memoria (evidencia volátil).

**Gestión de identidades y reseteo de cuentas**: Con los controladores de dominio comprometidos, es obligatorio resetear las contraseñas de todos los administradores y forzar el cierre de sesiones activas. No sirve de nada contener si el atacante sigue teniendo credenciales válidas.

**Filtrado estricto de la conexión a Internet**: Configuraría el firewall perimetral para bloquear todo el tráfico de salida hacia IPs desconocidas, permitiendo solo lo esencial para el negocio. Esto dificulta que el ransomware se comunique con su servidor de control (C2) para recibir órdenes o exfiltrar más datos.

**Auditoría de Backups y Plan de Comunicación**: Paralizaría cualquier restauración hasta confirmar que las copias son íntegras y no están infectadas. Al mismo tiempo, activaría el protocolo de comunicación con el personal, el equipo legal y las autoridades (INCIBE/AEPD) para cumplir con la normativa y gestionar la crisis.

**Plan de comunicación y notificación legal**: Alertaría a todo el personal con instrucciones claras para evitar que el incidente crezca. Además, coordinaría con el equipo legal y de comunicación la notificación a instituciones gubernamentales (como el INCIBE o la AEPD) para cumplir con la normativa vigente y gestionar la reputación de la empresa.

## 2. Tarea 2
