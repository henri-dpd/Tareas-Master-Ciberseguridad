# Tarea OSINT

## Ram

Comenzado análisis 2026-04-27 - 15:20:00, hash SHA256 del file `ram.raw`: `A0AD93B20CD9294F9D49947E87675C12159E3D96AE0D3C5A547F232630B0B240`.

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
