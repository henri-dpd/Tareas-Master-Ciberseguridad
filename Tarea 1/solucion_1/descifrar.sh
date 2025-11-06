#!/bin/bash
set -e

USER_KEY_HEX="00112233445566778899aabbccddeeff"
DOCS_DIR="solucion_1/cifrados"
OUTPUT_DIR="solucion_1/descifrados"
OPENSSL="openssl.exe"
export OPENSSL_CONF="C:\Program Files\OpenSSL-Win64\bin\openssl.cfg"

mkdir -p "$OUTPUT_DIR"

echo "Descifrando ficheros con Argon2id + AES-256-CBC"

for meta in "$DOCS_DIR"/*.meta; do
  base=$(basename "$meta" .meta)
  enc="$DOCS_DIR/$base.enc"

  # Leer metadatos
  source "$meta"

  # Derivar clave igual que al cifrar
  KEY_HEX=$($OPENSSL kdf -keylen 32 \
    -kdfopt pass:hex:$USER_KEY_HEX \
    -kdfopt salt:hex:$salt \
    -kdfopt iter:3 \
    -kdfopt memcost:65536 \
    -kdfopt lanes:1 \
    ARGON2ID | xxd -p -c 256)

  echo "Descifrando $base ..."
  "$OPENSSL" enc -d -aes-256-cbc \
    -in "$enc" \
    -out "$OUTPUT_DIR/$base" \
    -K "$KEY_HEX" \
    -iv "$iv" \
    -nosalt

  echo "$base descifrado → $OUTPUT_DIR/$base.dec"
  echo "--------------------------------------------"
done

echo "Todos los archivos fueron descifrados correctamente"
