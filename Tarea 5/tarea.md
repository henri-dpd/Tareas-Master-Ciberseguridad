# GUÍA TÉCNICA: CONSTRUCCIÓN DE FIRMWARE PERSONALIZADO (VOCORE2)

Este documento describe la secuencia exacta de pasos para generar el firmware que cumple con los requisitos de red, software y binarios de usuario.

---

## PASO 1: Configuración del Target (Hardware)
Antes de añadir archivos o paquetes, es fundamental definir el hardware para que el kernel y los drivers sean los correctos.

1. Ejecutar el menú de configuración:
   $ make menuconfig

2. Seleccionar las siguientes opciones para VoCore2 (No-Lite):
   - Target System: "MediaTek Ralink MIPS"
   - Subtarget: "MT76x8 based boards"
   - Target Profile: "VoCore2"

*Nota:* Esta selección aplica los 'offsets' de memoria correctos para la flash de 16MB, como se determinó en las tareas de ingeniería inversa.

---

## PASO 2: Selección de Software (Aircrack-ng)
Con el hardware definido, se añade el paquete solicitado desde los repositorios de OpenWrt.

1. Dentro de 'make menuconfig', navegar a:
   > Network --->
     > Wireless --->
       <*> aircrack-ng

2. [cite_start]Esto asegura que el binario 'aircrack-ng' se incluya en /usr/bin/[cite: 1, 2].

---

## PASO 3: Preparación del 'Filesystem Overlay'
Este paso es el que permite "inyectar" tus archivos personales (IP y Binario C) directamente en la imagen final.

1. Crear la estructura de carpetas en la raíz del SDK:
   $ mkdir -p files/etc/config
   $ mkdir -p files/root

---

## PASO 4: Punto 1 - Configuración de Red (IP Estática)
Se sobreescribe el archivo de red por defecto con la configuración de IP fija requerida.

1. Crear el archivo: `files/etc/config/network`
2. [cite_start]Configuración aplicada[cite: 3]:
   config interface 'lan'
       option type 'bridge'
       option ifname 'eth0.1'
       option proto 'static'
       option ipaddr '192.168.250.251'
       option netmask '255.255.255.0'

---

## PASO 5: Punto 2 - Inclusión del Binario C (ejercicio3)
Se integra tu programa compilado para que aparezca en la carpeta personal del root.

1. Mover tu binario a la carpeta del overlay:
   $ cp ejercicio3 files/root/

2. Dar permisos de ejecución:
   $ chmod +x files/root/ejercicio3

[cite_start]*Nota:* El binario contiene la firma "TAREA 3 UCM 2025" y está compilado para arquitectura mipsel[cite: 1].

---

## PASO 6: Compilación Final
Se genera el archivo .bin unificando todo lo anterior.

1. Ejecutar: $ make -j$(nproc) V=s
2. El firmware resultante se encuentra en: 
   `bin/targets/ramips/mt76x8/openwrt-ramips-mt76x8-vocore_vocore2-squashfs-sysupgrade.bin`

---

## PASO 7: Verificación de Integridad
Para asegurar que el proceso fue exitoso antes de flashear:
$ strings [archivo.bin] | grep "supported_devices"
(Debe confirmar: "vocore,vocore2") [cite_start][cite: 1, 2].