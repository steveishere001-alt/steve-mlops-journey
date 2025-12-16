from pathlib import Path

# --- INICIO DE LA RECETA ---
print("--- PLANIFICACIÓN DE LA RECETA DE PASTEL ---")

# 1. Definimos el Almacén Total (Existencias - Lista 1)
ALMACEN_TOTAL = [
    "Harina_Trigo", "Azucar", "Huevo", 
    "Sal", "Pimienta", "Oregano"  # Estos dos no son para pastel!
]

# 2. Definimos el Plan de Pastel (Componentes Requeridos - Lista 2)
# Solo necesitamos 3 de las existencias.
PLAN_DE_PASTEL = ["Harina_Trigo", "Azucar", "Huevo"]

print(f"Almacén Total: {len(ALMACEN_TOTAL)} items. Receta necesita: {len(PLAN_DE_PASTEL)} items.")

# 3. Definimos la RUTA BASE
RUTA_BASE = Path("estructura_pastel_receta") 
print(f"\nPreparando estantería en: {RUTA_BASE.name}")

# --- 4. BUCLE DE AUTOMATIZACIÓN (La Línea de Montaje) ---
for ingrediente in PLAN_DE_PASTEL:
    
    # 4a. Construir la ruta completa
    ruta_ingrediente = RUTA_BASE / ingrediente
    
    # 4b. Intentar crear la carpeta
    try:
        ruta_ingrediente.mkdir(parents=True, exist_ok=True)
        print(f"✅ Contenedor CREADO para: {ingrediente}")
    except Exception as e:
        # Esto solo se ejecutaría si hay un error de permisos o ruta
        print(f"❌ ERROR al crear {ingrediente}: {e}")

print("--- ESTRUCTURA DE COMPONENTES FINALIZADA ---")