#!/usr/bin/env python3
"""
Mi primer script de datos: contar líneas de un CSV.
Curso 1 – Día 1 – Steve
"""
from pathlib import Path

csv_path = Path("data/raw/penguins.csv")

try:
    lines = csv_path.read_text(encoding="utf-8").splitlines()
    print(f"Líneas totales: {len(lines)}")
except FileNotFoundError:
    print("Archivo no encontrado → es normal, hoy solo validamos el entorno.")
