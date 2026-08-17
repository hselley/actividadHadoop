#!/bin/bash

# Comprimir individualmente todos los archivos en el directorio actual
# (solo archivos, no directorios)

for archivo in *; do
    if [[ -f "$archivo" ]]; then
        echo "Comprimiendo: $archivo → $archivo.gz"
        gzip "$archivo"  # -k = "keep": conserva el original
        # O usa: gzip "$archivo"  # si quieres borrar el original tras comprimir
    fi
done
