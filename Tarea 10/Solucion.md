# Tarea Forense

## Ram

Comenzado análisis 2026-04-27 - 13:20:00 (UTC), hash SHA256 del file `ram.raw`: `A0AD93B20CD9294F9D49947E87675C12159E3D96AE0D3C5A547F232630B0B240`.

Comandos ejecutados con volatility:

```bash
.\volatility_2.6.exe -f 'D:\Master\Curso\Documentacion\15 - Documentación introducción a la práctica forense\Tarea\ram-001.raw' imageinfo

.\volatility_2.6.exe -f 'D:\Master\Curso\Documentacion\15 - Documentación introducción a la práctica forense\Tarea\ram-001.raw' --profile=Win7SP1x64 pslist

.\volatility_2.6.exe -f 'D:\Master\Curso\Documentacion\15 - Documentación introducción a la práctica forense\Tarea\ram-001.raw' --profile=Win7SP1x64 cmdline

.\volatility_2.6.exe -f 'D:\Master\Curso\Documentacion\15 - Documentación introducción a la práctica forense\Tarea\ram-001.raw' --profile=Win7SP1x64 consoles

.\volatility_2.6.exe -f 'D:\Master\Curso\Documentacion\15 - Documentación introducción a la práctica forense\Tarea\ram-001.raw' --profile=Win7SP1x64 hashdump

.\volatility_2.6.exe -f 'D:\Master\Curso\Documentacion\15 - Documentación introducción a la práctica forense\Tarea\ram-001.raw' --profile=Win7SP1x64 netscan
```

Adicionalmente se buscó en las herramientas CrackStation y Hashes.com el hash de la contraseña encontrado y se encontró una constraseña correspondiente a ese hash

| Hash                             | Hash Type | Result    |
| -------------------------------- | --------- | --------- |
| fc525c9683e8fe067095ba2ddc971889 | NTLM      | Passw0rd! |

---

Resumen de Hallazgos Forenses - Memoria RAM (Caso Murciélago)

1. Información de la Evidencia y Metodología
   Archivo: ram-001.raw

Perfil de Volatility: Win7SP1x64

Integridad: Hash calculado mediante Get-FileHash (SHA-256).

Contexto: El sistema analizado pertenece al usuario IEUser en una máquina con Windows 7 (distribución de Microsoft para pruebas).

2. Resolución Punto 1: Identificación de Credenciales
   Mediante el volcado de la base de datos SAM (hashdump) y el uso de técnicas de Rainbow Tables (CrackStation), se han identificado las siguientes credenciales:

Usuario: IEUser (SID: 1000)

Hash NTLM: fc525c9683e8fe067095ba2ddc971889

Contraseña en texto plano: Passw0rd!

Nota: La cuenta de Administrador comparte la misma contraseña.

3. Resolución Punto 2: Ejecución de Comandos y Borrado de Rastro
   El análisis de los buffers de consola (consoles) revela una actividad sospechosa realizada desde un terminal de Administrador:

Comandos ejecutados:

ipconfig: Verificación de la dirección IP local (192.168.65.135).

cd Desktop: Navegación al escritorio del usuario.

del HashMyFiles.cfg: Acción crítica. Se eliminó el archivo de configuración de la herramienta HashMyFiles para borrar el registro de integridad de los archivos manipulados, evitando la papelera de reciclaje.

Fichero eliminado: HashMyFiles.cfg

4. Hallazgos Adicionales: Exfiltración y Persistencia
   El análisis de red (netscan) y procesos (pslist/cmdline) confirma la infraestructura utilizada para la fuga de información:

IP de Destino (Exfiltración): Se detectó una conexión cerrada hacia la IP pública 200.228.36.6, identificada como el posible servidor del competidor.

Servicios Activos de Exfiltración:

sshd.exe (Puerto 22): Servidor SSH activo para túneles cifrados.

hMailServer.exe (Puertos 25, 110, 143, 587): Servidor de correo local configurado para envío de datos.

Binario Sospechoso: Ejecución de key.exe (PIDs 3856, 3184) desde el escritorio (C:\Users\IEUser\Desktop\key.exe), posible herramienta de captura o malware.

5. Próximos pasos (Análisis de Disco VMDK)
   Recuperar el archivo HashMyFiles.cfg mediante Autopsy.

Analizar los logs de envío de hMailServer para identificar destinatarios de los datos económicos.

Examinar la línea de tiempo de acceso a archivos en el escritorio y documentos.

Sugerencia: Si ya vas a pasar al disco, no olvides mencionar en tu informe que la IP 200.228.36.6 es la prueba clave que conecta el equipo interno con el exterior. ¿Quieres que te ayude a estructurar el informe final (Punto 3) siguiendo la normativa ISO que menciona tu temario?

---

## FTK Imager

Iniciado el analisis a las 2026-04-29 - 18:40:00 (UTC) de la imagen `IE11-Win7-VMWare-disk1-002.vmdk` con un hash: `60919A3ADC8450FA7E720EE68F6815D2179673C21C1844F198D7E45B38497068`

Otros comandos ejecutados para leer los lnk que tenemos en user > IEUser > AppData > Microsoft > Windows > Roaming > Recent

```bash
.\LECmd.exe -d 'D:\Master\Curso\Tareas\Tareas Master Ciberseguridad\Tarea 10\Evidencias\FTK Imager\Roaming_Microsoft_Windows_Recent' --all > output.txt
```

He analizado el output.txt que generaste con LECmd. Al procesar todos los archivos .lnk, has obtenido la cronología exacta y el mapa de actividad del atacante.Aquí tienes las rutas y los datos más interesantes que debes incluir en tu informe para el máster:1. El objetivo principal: Plan_de_cuentas.xlsEste es el archivo de exfiltración. Los metadatos de LECmd revelan:Ruta Original: C:\Users\IEUser\Documents\Documentacion empresa\Plan_de_cuentas.xlsFechas Críticas:Created: 2021-03-19 10:18:14 (Cuando se puso en esa carpeta).Last Accessed: 2021-03-23 11:08:31 (Momento exacto en que el atacante lo abrió antes de borrarlo).Interés Forense: Confirma que el archivo financiero existió y fue manipulado justo antes de que tú capturaras la RAM el día 23.2. La "Caja de Herramientas" en DownloadsEl reporte muestra que el usuario interactuó con los instaladores que vimos antes. Lo más relevante es la ruta de volumen:Herramientas: hMailServer-5.6.7-B2425.exe, Thunderbird Setup 78.8.1.exe y LibreOffice_7.1.1_Win_x64.msi.Interés: El atacante preparó el sistema el día 19 de marzo. Esto no fue un error accidental, fue un ataque planeado durante 4 días.3. Las pruebas de robo de credenciales: passwords.txtHay dos archivos muy sospechosos en la carpeta de documentos de IEUser:Rutas: C:\Users\IEUser\Documents\passwords.txt y C:\Users\IEUser\Documents\pass.txt.Interés: El atacante abrió estos archivos el 23 de marzo a las 17:27:53. Esto indica que, además de los datos financieros, se llevó una lista de contraseñas.4. Actividad Antiforense: DumpIt.exeRuta: C:\Users\IEUser\Desktop\DumpIt.exeInterés: El .lnk registra que se ejecutó el 23 de marzo a las 17:54:24. Como el archivo original tenía una X roja en FTK Imager, esto prueba que el atacante usó la herramienta y luego intentó borrarla para no dejar rastro de su propia actividad de captura.Resumen de rutas clave para tu Informe de Solución:ArchivoRuta detectada por LECmdImportanciaPlan de Cuentas..\Documents\Documentacion empresa\Plan_de_cuentas.xlsEvidencia de exfiltración de datos.Passwords..\Documents\passwords.txtEvidencia de robo de credenciales.Flag 2..\Documents\Documentacion empresa\flag2.txtEl mensaje de "buen camino" que encontraste.Key.exe..\Desktop\malware\key.exeEl malware que vimos en la RAM (si aparece el .lnk).Conclusión para el punto "Hallar el nombre":El nombre del archivo filtrado es Plan_de_cuentas.xls. Fue accedido por última vez el 23/03/2021 a las 11:08:31 (hora UTC, recuerda ajustar a la hora local de la máquina si es necesario).

---

Luego de ello analizamos $MFT para ver los archivos eliminados cone stos comandos:

```bash
.\MFTECmd.exe -f 'D:\Master\Curso\Tareas\Tareas Master Ciberseguridad\Tarea 10\Evidencias\FTK Imager\$MFT' --csv 'D:\Master\Curso\Tareas\Tareas Master Ciberseguridad\Tarea 10\Evidencias\FTK Imager' --csvf analisis_mft.csv --re "Users\\IEUser"

Select-String -Path ".\analisis_mft.csv" -Pattern ",True," | Select-Object -First 500 > mft_borrados_resumen.csv
```

resumen de las claves halladas tras procesar la MFT con MFTECmd, detallando rutas, estados y la cronología del ataque:1. El Objetivo del Robo: Plan_de_cuentas.xlsEs la prueba principal de la exfiltración.Ruta detectada: .\Users\IEUser\Documents\Documentacion empresa\Plan_de_cuentas.xlsEstado: IsDeleted: True (Marcado como borrado).Fechas Clave:Creación: 19/03/2021 (Coincide con la llegada de las herramientas del atacante).Última Modificación/Acceso: 23/03/2021 a las 11:08:31.Relevancia: Confirma que el archivo financiero fue manipulado y eliminado justo antes de que se realizara la captura de memoria.2. El Artefacto Malicioso: key.exeLa MFT confirma la ubicación física del malware que vimos activo en la RAM.Ruta detectada: .\Users\IEUser\Downloads\malware\key.exeEstado: IsDeleted: True.Relevancia: El hecho de estar dentro de una carpeta creada específicamente con el nombre "malware" denota intencionalidad clara. Al estar borrado pero presente en la MFT, demuestra que el atacante intentó limpiar el ejecutable tras infectar el sistema.3. Ficheros de Configuración de Correo y RedLa MFT registra la creación de carpetas para herramientas de exfiltración.Rutas detectadas:.\Program Files (x86)\hMailServer\.\Users\IEUser\AppData\Roaming\Thunderbird\Fechas: Todas las entradas de instalación apuntan al 19/03/2021.Relevancia: Prueba que el sistema fue "armado" con 4 días de antelación para poder mover los datos robados.4. Recolección de Credenciales: passwords.txtRutas detectadas: \* .\Users\IEUser\Documents\passwords.txt.\Users\IEUser\Documents\pass.txtEstado: IsDeleted: True.Relevancia: El atacante no solo buscaba el Excel, sino que recolectó contraseñas en texto plano para asegurar su persistencia o acceso a otros niveles de la infraestructura.5. Persistencia Remota: Carpeta .sshRuta detectada: .\Users\IEUser\.ssh\Archivos internos: environment, authorized_keys (encontrados vía FTK pero confirmados por la estructura de directorios en MFT).Relevancia: Confirma la configuración de un túnel cifrado. La MFT muestra que esta carpeta fue accedida/modificada durante el periodo del ataque.6. Evidencia Confesional: flag2.txtRuta detectada: .\Users\IEUser\Documents\Documentacion empresa\flag2.txtRelevancia: Este archivo es un "artefacto de autoría". El atacante lo dejó en la misma ruta que el archivo sustraído para confirmar el éxito de la operación.Resumen Cronológico según la MFT:19/03/2021: El atacante crea la estructura de directorios en Downloads (malware) y Documents (documentación empresa). Instala el software de soporte (hMailServer/LibreOffice).23/03/2021 (Mañana): Se accede al archivo Plan_de_cuentas.xls por última vez.23/03/2021 (Tarde): Se ejecutan las tareas de limpieza. El atacante marca como borrados (IsDeleted: True) el malware, los archivos de texto con contraseñas y el propio Excel robado.Conclusión técnica para el informe: La $MFT$ demuestra que, a pesar de los esfuerzos de borrado del sospechoso, existe una correlación temporal perfecta entre la instalación de herramientas, el acceso a información sensible y el borrado final de evidencias.

---

🛡️ Informe de Hallazgos Forenses (Fase de Disco - Revisado)

1. Evidencia de Ejecución de Software (Análisis de C:\Windows\Prefetch)
   Afirmación: Se confirma la ejecución de herramientas de red, oficina y código malicioso en la sesión del usuario.

Justificación Técnica:

Artefacto: Archivos .pf extraídos de la carpeta Prefetch.

Hallazgo: La existencia de archivos como HMAILSERVER.EXE-59392E89.pf, THUNDERBIRD.EXE-EDED9AF7.pf y, crucialmente, KEY.EXE-A7310F00.pf.

Trazabilidad: Estos archivos demuestran no solo que el software estaba en el disco, sino que se ejecutó. El análisis de los archivos Prefetch permite determinar la fecha y hora de la última ejecución y el número de veces que se abrieron, vinculando el malware key.exe directamente con la actividad del sistema.

2. Preparación y Armamento (Evidencia en Downloads)
   Afirmación: El sistema fue modificado el 19/03/2021 para facilitar la exfiltración de datos.

Justificación Técnica:

Evidencia en FTK Imager: Presencia de instaladores (hMailServer, Thunderbird, LibreOffice) en la ruta \Users\IEUser\Downloads.

Carpeta de Malware: Localización de la carpeta \Users\IEUser\Downloads\malware. Aunque el ejecutable pueda haber sido borrado posteriormente, la existencia de la carpeta y su registro en la $MFT (Master File Table) prueban su disposición en el disco.

3. Identificación del Objetivo y Exfiltración
   Afirmación: El activo sustraído fue el documento Plan_de_cuentas.xls.

Justificación Técnica:

Análisis de LNK (LECmd): El archivo Plan_de_cuentas.xls.lnk en la carpeta Recent del usuario apunta a la ruta original \Documents\Documentacion empresa\.

Evidencia Confesional: Localización y apertura en FTK Imager del archivo flag2.txt en la carpeta del objetivo, donde el atacante declara explícitamente: "Los archivos filtrados eran .xls".

Acceso a Credenciales: Se confirma la apertura de passwords.txt y pass.txt, evidenciada por sus respectivos accesos directos en el historial de archivos recientes.

4. Persistencia y Comunicación Externa
   Afirmación: El atacante utilizó el protocolo SSH para mantener un túnel de comunicación cifrado.

Justificación Técnica:

Artefactos SSH: Presencia de la carpeta \Users\IEUser\.ssh y el archivo environment.

Correlación: Esto justifica la persistencia del puerto 22 abierto y explica cómo el atacante pudo mover archivos de gran tamaño (como el Excel) sin activar alertas de inspección de paquetes simples.

5. Acciones de Borrado (Post-Exfiltración)
   Afirmación: Tras cumplir sus objetivos, el atacante realizó un borrado de los archivos incriminatorios.

Justificación Técnica:

Estado en FTK Imager: Visualización de los archivos Plan_de_cuentas.xls y key.exe con la X roja.

Análisis de la $MFT: El registro de estos archivos en el CSV de la MFT muestra el flag IsDeleted: True. Esto prueba que el atacante intentó eliminar la evidencia física del disco después de la ejecución.

📝 Resumen Narrativo para la Redacción
"El análisis forense del disco revela una intrusión planificada iniciada el 19/03/2021. El usuario IEUser instaló herramientas de correo y oficina para preparar la salida de datos. Mediante la ejecución de un código malicioso denominado key.exe (cuya ejecución está certificada por los archivos Prefetch localizados), el atacante procedió a capturar credenciales y acceder al documento Plan_de_cuentas.xls. Tras exfiltrar la información a través de un túnel SSH, se procedió al borrado de los ejecutables y documentos, rastro que ha sido recuperado mediante el análisis de la MFT y los archivos LNK."

Nota sobre DumpIt: Eliminado de la narrativa del ataque. Se asume como la herramienta técnica utilizada exclusivamente para la adquisición forense de la memoria RAM previa al análisis del disco.

---

### Kape

Extraccion de !BasicCollection, !SANS_Triage, WebBrowsers y LNKFilesAndJumpLists, ademas se hace un parser con el module !EZParser.

Comandos usados en kape:

```bash
.\kape.exe --tsource E: --tdest "D:\Master\Curso\Tareas\Tareas Master Ciberseguridad\Tarea 10\Evidencias\Triage_Kape\Targets" --tflush --target !BasicCollection,!SANS_Triage,WebBrowsers,LNKFilesAndJumpLists --mdest "D:\Master\Curso\Tareas\Tareas Master Ciberseguridad\Tarea 10\Evidencias\Triage_Kape\Modules" --mflush --module !EZParser --mef csv --gui

# Herramienta amcache
 .\AmcacheParser.exe -f "D:\Master\Curso\Tareas\Tareas Master Ciberseguridad\Tarea 10\Evidencias\Triage_Kape\Targets\E\Windows\AppCompat\Programs\Amcache.hve" --csv "D:\Master\Curso\Tareas\Tareas Master Ciberseguridad\Tarea 10\Evidencias\Triage_Kape"
```

link virus total del malware key.exe: `https://www.virustotal.com/gui/file/d3e05795d760d7ee9d935cae5a3b9f71c064b27788054ab2f8b5d090314dceb4/detection`

---

Informe Forense Integral: Análisis del Compromiso "Key.exe"

1. Vector de Entrada e Identificación del Malware
   Origen Externo: Mediante el análisis de la $MFT, se confirmó que los archivos sospechosos poseían el identificador .Zone.Identifier=3, lo que prueba técnicamente que fueron descargados de internet.

Naturaleza de la Amenaza: El análisis de Amcache permitió obtener el hash SHA-1 de key.exe, el cual arrojó 42 detecciones positivas en VirusTotal. Se identifica como un Troyano/Keylogger basado en Python diseñado para el robo de credenciales.

2. Evidencias de Ejecución y Persistencia
   Ejecución Recurrente: El artefacto Prefetch (PECmd) registró un total de 8 ejecuciones de key.exe.

Monitoreo del Atacante: Se detectó la ejecución del Administrador de Tareas (taskmgr.exe) en la misma ventana de tiempo, sugiriendo que el atacante o el malware vigilaban los procesos del sistema.

Persistencia por Replicación: Se localizaron copias del malware en rutas críticas del sistema: C:\Windows\System32\key.exe y C:\Windows\SysWOW64\key.exe, una técnica para dificultar la desinfección y ocultarse entre procesos legítimos.

Análisis de Registro: Tras interrogar las colmenas NTUSER.DAT y SOFTWARE con WRR, se descartó el uso de las llaves Run estándar, lo que confirma que el malware utiliza métodos de persistencia más avanzados o manuales para evadir herramientas de seguridad básicas.

3. Actividad del Usuario e Interacción con Datos
   Atribución de Sesión: A través de WinLogonView, se identificaron múltiples sesiones interactivas (Logon Type 2) del usuario IEUser durante los días 19 y 23 de marzo de 2021.

Acceso a Información Sensible: El análisis de archivos LNK (LECmd) demostró de forma irrefutable que se abrieron documentos financieros críticos:

CLIENTES DEL BANCO.xls.

Plan_de_cuentas.xls.

Estado de cuenta bancario.xls.

4. Maniobras Anti-Forense (Destrucción de Pruebas)
   Borrado Selectivo: El análisis de la $MFT reveló que los documentos financieros mencionados fueron eliminados del sistema el 23/03/2021 a las 23:08:59.

Intencionalidad: El borrado ocurrió justo después de las últimas ejecuciones del malware y el acceso a los datos, confirmando un intento deliberado de ocultar el rastro de la exfiltración de información.

Conclusión Final
La investigación demuestra un ataque dirigido exitoso. El atacante logró introducir un keylogger mediante descarga directa, obtuvo persistencia en directorios del sistema, accedió a la base de datos de clientes y estados bancarios, y finalmente ejecutó tareas de limpieza eliminando los archivos comprometidos para frustrar la respuesta ante incidentes.

Este análisis exhaustivo, basado en la correlación de Prefetch, LNK, MFT, Registry, Logs de inicio de sesión y Amcache, proporciona una cadena de custodia y evidencia completa para el caso.
