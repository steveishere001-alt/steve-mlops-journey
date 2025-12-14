from pathlib import Path

# --- 1. Definición de Variables (INPUTS) ---
NOMBRE_ARCHIVO = "datos_maestros.txt"  # str: El nombre del archivo
CONTENIDO_INICIAL = "ID,Nombre,Valor\n1,Prueba,10" # str: Contenido a escribir
ruta_datos = Path('data') / NOMBRE_ARCHIVO # Uso de Pathlib para crear la ruta
estado_operacion = False # bool: Flag inicial de estado

# --- 2. Lógica Condicional y Creación (IF/ELSE) ---
print("\n--- INICIO DE VALIDACIÓN ---")

if ruta_datos.exists():
    # Bloque IF: El archivo existe
    print(f"✅ El archivo '{NOMBRE_ARCHIVO}' ya existe en: {ruta_datos}")
    estado_operacion = True 
else:
    # Bloque ELSE: El archivo NO existe
    print(f"⚠️ El archivo '{NOMBRE_ARCHIVO}' no se encontró. Creando...")
    
    # Crea la carpeta 'data/' si no existe.
    ruta_datos.parent.mkdir(exist_ok=True) 
    
    # Escribe el contenido.
    ruta_datos.write_text(CONTENIDO_INICIAL)
    
    print(f"📝 Archivo creado exitosamente en {ruta_datos}")
    estado_operacion = True

# --- 3. Diagnóstico de Tipos (type()) ---
print("\n--- Diagnóstico de Tipos ---")

# Verificar si el flag es un booleano (Diagnóstico)
if type(estado_operacion) is bool:
    print(f"✅ Estado de Operación: {estado_operacion} (<class 'bool'>, Correcto)")
else:
    print("❌ ERROR: La variable de estado no es un booleano.")
    
print("--------------------------\n")