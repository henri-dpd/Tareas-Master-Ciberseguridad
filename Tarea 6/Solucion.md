# Tarea detección, correlación y acción

## 1.2 Ficheros STIX

- ¿Quién es el autor del informe?

  La Oficina Federal de Investigaciones (FBI), la Agencia de Seguridad Cibernética y de Infraestructuras (CISA) y el Centro Multiestatal de Intercambio y Análisis de Información (MS-ISAC) publicaron este informe en conjunto.

- ¿De qué adversario trata el informe?

  Vice Society operando con el ransomware Medusa en su variante como RaaS

- ¿Cómo clasificarías a este adversario dentro de los seis tipos que hemos visto?

  Lo clasificaría como Cibercrimen porque su motivación principal es el beneficio económico mediante la extorsión.

- ¿En qué año se identificó por primera vez actividad de este adversario?

  Fue identificado por primera vez en junio de 2021.

- ¿Está relacionado con algún otro adversario conocido?

  No está relacionada con la variante MedusaLocker ni con la variante de malware móvil Medusa. Pero sí existe una asociación técnica entre el nombre Vice Society y la operación Medusa Ransomware confirmada por las referencias externas

- ¿Qué vulnerabilidades suele explotar este adversario? (CVE y explicación breve del
  producto afectado y la vulnerabilidad)

  Principalmente de dos fallos en programas que las empresas usan para gestionar datos: el CVE-2023-0669, que afecta a GoAnywhere MFT y les permite ejecutar código a distancia para tomar el control del servidor; y el CVE-2022-24990, que afecta a los discos duros en red (NAS) de la marca TerraMaster, permitiéndoles enviar comandos al equipo sin necesidad de contraseña para robar o borrar la información.

- ¿Qué 5 direcciones de e-mail aparecen como indicadores?

  1. key.medusa.serviceteam@protonmail.com
  2. medusa.support.team@protonmail.com
  3. medusa.recovery.help@protonmail.com
  4. help.medusa.service@protonmail.com
  5. support.medusa.key@protonmail.com

- ¿Qué finalidad crees que cumplen estas direcciones de e-mail para el adversario y sus
  víctimas?

  Sirven como canal de Mando y Control (C2) y negociación de forma que permiten a las víctimas contactar con los atacantes para recibir instrucciones de pago y se utilizan para gestionar la entrega de las llaves de descifrado tras el pago del rescate.

- ¿Qué técnicas descritas en la matriz de MITRE ATT&CK utiliza el adversario para el
  comando y control (TA0011 - Command and Control)? (Código identificador y nombre de
  la técnica / subtécnica)

  - T1071.001 - Application Layer Protocol: Web Protocols: Utilizan protocolos web estándar (como HTTP o HTTPS) para que el tráfico malicioso se camufle entre la navegación normal de la empresa y pase desapercibido por los firewalls.
  - T1105 - Ingress Tool Transfer: Esta técnica la usan para descargar herramientas adicionales o piezas de malware desde sus servidores externos hacia el equipo de la víctima una vez que ya han conseguido entrar.

- Entre las herramientas utilizadas por el adversario se encuentran Mimikatz, Anydesk y
  Certutil. Para cada una de ellas, contesta a las siguientes preguntas:

  - ¿Se encuentra por defecto en Windows?
  - ¿La categorizarías como malware?
  - Si no la categorizarías como malware, ¿por qué aparece el informe?

  1. Mimikatz
     ¿Se encuentra por defecto en Windows? No. Es una herramienta externa que el atacante debe descargar e instalar en el equipo víctima.
     ¿La categorizarías como malware? Sí. Aunque se usa en auditorías éticas, su función principal es el robo de credenciales (extracción de contraseñas de la memoria), por lo que casi cualquier antivirus la detecta directamente como software malicioso (HackTool).
     ¿Por qué aparece en el informe? Porque es la herramienta "estrella" que usa Vice Society para volcar las contraseñas de la memoria de Windows y así conseguir las claves del Administrador del Dominio.
  2. Anydesk
     ¿Se encuentra por defecto en Windows? No. Es un software de terceros muy popular para soporte técnico remoto.
     ¿La categorizarías como malware? No. Es una herramienta legítima y legal de administración remota.
     ¿Por qué aparece en el informe? Porque los atacantes la instalan para mantener la persistencia. Si el administrador de la red cierra sus "puertas traseras" habituales, ellos pueden seguir entrando cómodamente a través de Anydesk como si fueran un técnico de soporte real.
  3. Certutil
     ¿Se encuentra por defecto en Windows? Sí. Es una utilidad de línea de comandos nativa de Windows que sirve para gestionar certificados digitales.
     ¿La categorizarías como malware? No. Es un componente oficial y legítimo del sistema operativo.
     ¿Por qué aparece en el informe? Porque tiene una función que permite descargar archivos de internet (mediante el parámetro -urlcache). Los atacantes la "abusan" para descargar sus virus o scripts maliciosos saltándose algunos filtros de seguridad, ya que el sistema confía en el proceso certutil.exe por ser de Microsoft.

## 1.3 Expresiones Regulares

¿Cúal es el nombre de equipo (FQDN) del propio firewall del que proviene la traza
syslog?

paloalto.evil.corp

| Atributo | Valor | Expresión regular | Grupo de captura |
| :--- | :--- | :--- | :--- |
| **Categoría** | THREAT | `cat\s*=\s*(?P<categoria>[^\|]+)` | categoria |
| **Subtipo** | virus | `Subtype\s*=\s*(?P<subtipo>[^\|]+)` | subtipo |
| **Timestamp** | May 06 2025 16:43:53 GMT | `devTime\s*=\s*(?P<timestamp>[^\|]+)` | timestamp |
| **IP origen** | 10.2.75.41 | `src\s*=\s*(?P<ip_origen>[^\|]+)` | ip_origen |
| **IP destino** | 192.168.178.180 | `dst\s*=\s*(?P<ip_destino>[^\|]+)` | ip_destino |
| **Regla** | Test-1 | `RuleName\s*=\s*(?P<regla>[^\|]+)` | regla |
| **Usuario** | ealderson | `usrName\s*=\s*(?P<usuario>[^\|]+)` | usuario |
| **Aplicación** | web-browsing | `Application\s*=\s*(?P<aplicacion>[^\|]+)` | aplicacion |
| **Sistema Virtual** | vsys1 | `VirtualSystem\s*=\s*(?P<sistema_virtual>[^\|]+)` | sistema_virtual |
| **Zona Origen** | INSIDE-ZN | `SourceZone\s*=\s*(?P<zona_origen>[^\|]+)` | zona_origen |
| **Zona Destino** | OUTSIDE-ZN | `DestinationZone\s*=\s*(?P<zona_destino>[^\|]+)` | zona_destino |
| **Puerto Origen** | 63508 | `srcPort\s*=\s*(?P<puerto_origen>\d+)` | puerto_origen |
| **Puerto Destino** | 80 | `dstPort\s*=\s*(?P<puerto_destino>\d+)` | puerto_destino |
| **Protocolo** | tcp | `proto\s*=\s*(?P<protocolo>\w+)` | protocolo |
| **URL** | [badguys.co/du/uploads/08052018_UG_FAQ.pdf]() | `Miscellaneous\s*=\s*"(?P<url>[^"]+)"` | url |
| **Categoría URL** | educational-institutions | `URLCategory\s*=\s*(?P<categoria_url>[^\|]+)` | categoria_url |
| **Dominio** | badguys.co | `Miscellaneous\s*=\s*"(?P<dominio>[^\/"]+)` | dominio |
| **Nombre Fichero** | 08052018_UG_FAQ.pdf | `Miscellaneous\s*=\s*"[^"]*\/(?P<nombre_fichero>[^"\/]+)"` | nombre_fichero |
| **Firma** | trojan/PDF.gen.eiez | `ThreatID\s*=\s*(?<firma>[^(\s]+)` | firma |
| **ID firma** | 268198686 | `ThreatID\s*=\s*.*?\((?P<id_firma>\d+)\)` | id_firma |

Nota: En el caso de SourceZone el pdf al copiar inserta un salto de línea, así que asumiq ue esto podría pasar en otros atributos e inserte \s* para que se encuentre el atributo buscado no importa si hay saltos de lineas o espaciones inesperados antes o despues de los símbolos de igualdad.

