import csv
import random
from datetime import timedelta, date

# Configuración
start_date = date(2026, 1, 1)
num_files = 50
records_per_file = 1000000

# Categorías y pesos (para que algunas aparezcan más seguido)
categories = [
    "ropa", "alimentos", "electrónica", "hogar", "deportes",
    "libros", "juguetes", "cosmética", "automotriz", "servicios"
]

# Pesos: más frecuentes al inicio
weights = [15, 15, 12, 10, 10, 8, 7, 6, 5, 2]  # suman 90 → normalizamos

def weighted_choice(categories, weights):
    total = sum(weights)
    r = random.uniform(0, total)
    cumulative = 0
    for cat, w in zip(categories, weights):
        cumulative += w
        if r <= cumulative:
            return cat
    return categories[-1]

# Rango de precios (aprox por categoría)
price_ranges = {
    "ropa": (20, 200),
    "alimentos": (5, 80),
    "electrónica": (150, 800),
    "hogar": (30, 400),
    "deportes": (15, 250),
    "libros": (10, 60),
    "juguetes": (15, 120),
    "cosmética": (15, 150),
    "automotriz": (100, 1500),
    "servicios": (30, 600)
}

for i in range(num_files):
    current_date = start_date + timedelta(days=i)
    filename = f"ventas_{current_date}.csv"
    
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["categoria", "precio"])  # cabecera
        
        for _ in range(records_per_file):
            cat = weighted_choice(categories, weights)
            low, high = price_ranges[cat]
            price = random.randint(max(10, low), min(1500, high))  # límites seguros
            writer.writerow([cat, price])
    
    print(f"✅ Archivo generado: {filename}")
