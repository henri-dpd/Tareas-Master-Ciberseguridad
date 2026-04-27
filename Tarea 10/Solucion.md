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

| Hash | Hash Type | Result |
|------|-----------|--------|
| fc525c9683e8fe067095ba2ddc971889 | NTLM | Passw0rd! |

Resumen de lo que tengo para el Informe (Punto 3):
Punto 1 (Contraseña): El usuario `IEUser` tiene la contraseña `Passw0rd!`. Se pudo obtener extrayendo el hash NTLM de la RAM con Volatility (hashdump - `fc525c9683e8fe067095ba2ddc971889`) y rompiéndolo mediante una Rainbow Table online (CrackStation y Hashes.com).

Punto 2 (Borrado de rastro): Confirmaste que el usuario ejecutó el comando del `HashMyFiles.cfg` desde la consola (cmd.exe) para eliminar el archivo de configuración de una herramienta de integridad de ficheros, evitando así la papelera de reciclaje.
