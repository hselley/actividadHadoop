import csv
from collections import defaultdict

def calcular_promedio_por_rubro(archivo_csv):
    suma = defaultdict(float)
    conteo = defaultdict(int)

    try:
        with open(archivo_csv, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Usamos .get() para evitar KeyError si el encabezado es distinto
                categoria = row.get("categoria", "").strip()
                precio_str = row.get("precio", "").strip()
                
                if not categoria or not precio_str:
                    continue  # saltar líneas vacías o inválidas
                
                try:
                    precio = float(precio_str)
                    suma[categoria] += precio
                    conteo[categoria] += 1
                except ValueError:
                    print(f"⚠️ Valor de precio no válido: {precio_str}")
                    continue

        print("📊 Promedio por rubro:")
        print("-" * 30)
        for cat in sorted(suma.keys()):
            promedio = suma[cat] / conteo[cat]
            print(f"{cat:15} → {promedio:.2f}")

    except FileNotFoundError:
        print(f"❌ Archivo '{archivo_csv}' no encontrado.")
    except Exception as e:
        print(f"❌ Error: {e}")

# === Ejecutar con tu archivo ===
calcular_promedio_por_rubro("in/ventas_2026-01-01.csv")
