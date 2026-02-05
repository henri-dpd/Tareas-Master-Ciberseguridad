======================================================================
REPORTE DE AUDITORIA TECNICA: FIRMWARE VOCORE2 (UCM 2026)
======================================================================

1. IDENTIFICACION DEL HARDWARE Y METADATOS
----------------------------------------------------------------------
Se ha verificado mediante el analisis de metadatos JSON que el 
firmware corresponde al modelo VoCore2 estandar (no Lite).

* [cite_start]Target detectado: ramips/mt76x8 [cite: 1]
* [cite_start]Dispositivos soportados: ["vocore,vocore2","vocore2"] [cite: 1]
* [cite_start]Revision de compilacion: r32723-46129bbbf5 [cite: 1]

2. ESTRUCTURA DEL BINARIO (INGENIERIA INVERSA)
----------------------------------------------------------------------
Utilizando binwalk se identificaron los siguientes puntos de montaje:

* Kernel (LZMA): Offset 0x40 (64 decimal).
* FileSystem (Squashfs XZ): Offset 1946004 (0x1DB194).

3. VERIFICACION DE CONTENIDOS (SISTEMA DE ARCHIVOS)
----------------------------------------------------------------------
Tras la extraccion manual con 'dd' y 'unsquashfs', se confirman los 
siguientes hallazgos:

A. PERSISTENCIA DE RED:
El archivo /etc/config/network contiene la IP estatica configurada 
originalmente en la carpeta 'files/':
- [cite_start]IP: 192.168.250.251 [cite: 3]
- [cite_start]Mascara: 255.255.255.0 [cite: 3]
- [cite_start]Interfaz: LAN (bridge) [cite: 3]

B. BINARIO PERSONALIZADO:
El programa 'ejercicio3' se encuentra en /root/ con las siguientes 
caracteristicas:
- [cite_start]Firma de autoría: "TAREA 3 UCM 2025" [cite: 1]
- [cite_start]Arquitectura: mipsel_24kc (Little Endian) [cite: 1]
- [cite_start]Herramienta: GCC 14.3.0 musl-1.2.5 [cite: 1]

C. HERRAMIENTAS DE AUDITORIA:
- Aircrack-ng: Instalado en /usr/bin/aircrack-ng (134,355 bytes).

4. NOTAS SOBRE OFFSETS Y MEMORIA
----------------------------------------------------------------------
En base a las tareas realizadas el 17 de diciembre, se confirma el uso 
de los offsets mas grandes para el mapeo de memoria. Esto asegura que 
el sistema de archivos de 5.6 MB no colisione con las particiones 
criticas del Kernel en la flash de 16MB del VoCore2.

----------------------------------------------------------------------
FIN DEL REPORTE - ENTORNO KALI LINUX
======================================================================