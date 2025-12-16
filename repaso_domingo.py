from pathlib import Path

print("--- INICIO GESTIÓN DE INVENTARIO (exitencias KIT DE COMPONENTES) ---")

# 1. Definimos el Pallet/Lista (Nuestro Kit de Ensamblaje Básico de un Auto)
# Los corchetes [] representan la Lista de componentes.
kit_ensamblaje = [
    "frenos abs-031F",
    "frenos tambor regular-044f",
    "motor V6, 4.0-mo640",
    "motor 4t 2.5-mo425",
    "motor 8t 3.0-mo830",
    "chasis aluminio_aceroInox-c075A",
    "chasis acero inoxidable_fibradecarbono-c0A24",
    "kit interior piel-int001",
    "kit interior std-int000",
    "kit comp electrico pro-ele00A",
    "kit comp elecrtrico basic-ele00B",
    "componetes plasticos-pla32",
    "llantas90 -neu90",
    "llantas85 -neu 85"

]
print(f"✅ existencias de material para produciion {len(kit_ensamblaje)} componentes listos.")
# len() cuenta la cantidad de elementos en nuestro Kit (Lista).

# 2. El Diagnóstico con type()
print(f"El contenedor del Kit es de tipo: {type(kit_ensamblaje)}")

# 3. ¡Nos damos cuenta que el Motor_V6 es un subcomponente! (Necesitamos quitar el genérico)
# Usamos el método .remove() para quitar un elemento por su nombre.
kit_ensamblaje.remove("frenos tambor regular-044f")
print("➖ Quitamos 'Motor' (Se gestionará en otro sub-kit).")

# 4. ¡Añadimos el nuevo componente de alta seguridad! (Necesitamos añadirlo)
# Usamos el método .append() para añadir un elemento al final de la Lista.
kit_ensamblaje.append("Sistema_Control_Traccion")
print("➕ Añadimos 'Sistema_Control_Traccion'.")

print("\n--- KIT DE ENSAMBLAJE FINAL ---")
# Imprimimos la lista de componentes actualizada
print(kit_ensamblaje)

print(f"📢 Total final de componentes en el Kit: {len(kit_ensamblaje)}.")
print("--- FIN GESTIÓN DE INVENTARIO ---")
# --- NUEVO BLOQUE: CREACIÓN DE CARPETAS DE GESTIÓN ---
print("\n--- INICIO DE ESTRUCTURA DE ALMACÉN ---")

# 1. Definimos la ruta base para nuestros Kits
# Creamos una carpeta base "almacen_fabrica" en la raíz del proyecto.
RUTA_BASE = Path("almacen_fabrica") 

# 2. Recorremos el Pallet (Kit de Ensamblaje)
# El 'for' nos permite hacer la misma acción por cada elemento en la Lista.
for componente in kit_ensamblaje:
    
    # Usamos Pathlib para crear la ruta: almacen_fabrica / ID_de_Componente
    ruta_componente = RUTA_BASE / componente
    
    # Creamos la carpeta (el mkdir robusto)
    try:
        # parents=True crea la carpeta principal si no existe.
        # exist_ok=True evita que el script falle si ya ejecutamos esto.
        ruta_componente.mkdir(parents=True, exist_ok=True)
        print(f"📦 Creado almacén para: {componente}")
    except Exception as e:
        print(f"❌ Error al crear carpeta: {e}")

print("--- ESTRUCTURA DE ALMACÉN FINALIZADA ---")