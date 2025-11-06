#!/bin/bash
set -e

# ===== CONFIGURACIÓN =====
USER_KEY_HEX="00112233445566778899aabbccddeeff"  # Clave maestra de 128 bits
DOCS_DIR="solucion_1/docs"
OUTPUT_DIR="solucion_1/cifrados"
OPENSSL="openssl.exe"
export OPENSSL_CONF="C:\Program Files\OpenSSL-Win64\bin\openssl.cfg"

mkdir -p "$OUTPUT_DIR"

echo "Cifrando ficheros con Argon2id + AES-256-CBC"
echo "Clave maestra (hex): $USER_KEY_HEX"
echo "--------------------------------------------"

i=1
for file in "$DOCS_DIR"/*; do
  filename=$(basename "$file")
  echo "📄 Archivo #$i: $filename"

  # Generar salt aleatorio (16 bytes)
  SALT=$($OPENSSL rand -hex 16)

  # Derivar clave con Argon2id (32 bytes)
  KEY_HEX=$($OPENSSL kdf -keylen 32 \
    -kdfopt pass:hex:$USER_KEY_HEX \
    -kdfopt salt:hex:$SALT \
    -kdfopt iter:3 \
    -kdfopt memcost:65536 \
    -kdfopt lanes:1 \
    ARGON2ID | xxd -p -c 256)

  # Generar IV aleatorio (16 bytes para AES-CBC)
  IV_HEX=$($OPENSSL rand -hex 16)

  # Cifrar con AES-256-CBC
  "$OPENSSL" enc -aes-256-cbc \
    -in "$file" \
    -out "$OUTPUT_DIR/$filename.enc" \
    -K "$KEY_HEX" \
    -iv "$IV_HEX" \
    -nosalt

  # Guardar metadatos (salt + iv)
  {
    echo "salt=$SALT"
    echo "iv=$IV_HEX"
  } > "$OUTPUT_DIR/$filename.meta"

  echo "Cifrado completado → $OUTPUT_DIR/$filename.enc"
  echo "Salt: $SALT"
  echo "Clave derivada: ${KEY_HEX:0:16}..."
  echo "--------------------------------------------"
  ((i++))
done

echo "Cifrado completado: todas las claves derivadas con Argon2id"
