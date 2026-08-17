import csv
import os
from collections import defaultdict
import glob

def calcular_promedios_globales(directorio="."):
    # Diccionarios para acumular sumas y conteos globales
    suma_global = defaultdict(float)
    conteo_global = defaultdict(int)

    # Buscar archivos CSV que empiecen con "ventas_" y terminen en .csv
    patron = os.path.join(directorio, "ventas_*.csv")
    archivos_csv = sorted(glob.glob(patron))

    if not archivos_csv:
        print(f"⚠️ No se encontraron archivos 'ventas_*.csv' en '{directorio}'.")
        return

    print(f"📁 Procesando {len(archivos_csv)} archivo(s) CSV...\n")

    # Opcional: también guardar promedios por archivo (si quieres comparar fechas)
    promedios_por_archivo = {}

    for archivo in archivos_csv:
        suma_archivo = defaultdict(float)
        conteo_archivo = defaultdict(int)

        try:
            with open(archivo, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Normalizar nombre de columna (puede ser "categoria" o "categoría")
                    categoria = row.get("categoria", "").strip() or row.get("categoría", "").strip()
                    precio_str = row.get("precio", "").strip()

                    if not categoria or not precio_str:
                        continue

                    try:
                        precio = float(precio_str)
                    except ValueError:
                        print(f"  ⚠️ Línea con precio inválido en '{archivo}': {row}")
                        continue

                    # Acumular en global y por-archivo
                    suma_global[categoria] += precio
                    conteo_global[categoria] += 1
                    suma_archivo[categoria] += precio
                    conteo_archivo[categoria] += 1

        except Exception as e:
            print(f"  ❌ Error al leer '{archivo}': {e}")
            continue

        # Calcular promedio por archivo (opcional)
        promedios_archivo = {
            cat: suma_archivo[cat] / conteo_archivo[cat]
            for cat in suma_archivo
        }
        promedios_por_archivo[archivo] = promedios_archivo

    # === Mostrar resultados globales ===
    print("=" * 45)
    print("📊 PROMEDIO GLOBAL POR RUBRO (todos los archivos)")
    print("=" * 45)
    print(f"{'Categoría':<18} {'Promedio':>12} {'Total registros':>15}")
    print("-" * 45)

    for cat in sorted(suma_global.keys()):
        promedio = suma_global[cat] / conteo_global[cat]
        print(f"{cat:<18} {promedio:>12.2f} {conteo_global[cat]:>15}")

    total_registros = sum(conteo_global.values())
    print("-" * 45)
    print(f"{'TOTAL':<18} {'-':>12} {total_registros:>15}")
    print("=" * 45)

    # === Opcional: mostrar promedios por archivo (últimos 3 como ejemplo) ===
    # descomentar si quieres ver detalles por fecha:
    """
    print("\n📅 Promedios por archivo (últimos 3 archivos procesados):")
    for archivo in list(promedios_por_archivo.keys())[-3:]:
        print(f"\n📂 {os.path.basename(archivo)}:")
        for cat in sorted(promedios_por_archivo[archivo].keys()):
            print(f"   {cat}: {promedios_por_archivo[archivo][cat]:.2f}")
    """

    return suma_global, conteo_global

# === Ejecutar ===
if __name__ == "__main__":
    # Puedes cambiar "." por la ruta de tu carpeta, ej: "/home/usuario/ventas"
    calcular_promedios_globales(".")
