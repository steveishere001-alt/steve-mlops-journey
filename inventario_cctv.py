#!/usr/bin/env python3
# Inventario básico CCTV - Steve
from pathlib import Path

lista_camaras = [
    "camara_entrada_001",
    "camara_entrada_002",
    "camara_entrada_003",
    "camara_Garage_004",
    "camara_Garage_006",
    "camara_pasillo_007",
    "camara_pasillo_008",
    "camara_cocina_009",
    "camara_escaleras_010",
    "camara_pasillo_interno_011",
    "camara_exterior_012"
]

print(f"Cámaras activas iniciales: {len(lista_camaras)} funcionando y grabando")
print()

# Bucle para agregar tantas cámaras como quiera el usuario 
        #Orden lógico: 
           #Pido entrada.
            #Si es "fin", salgo.
            #Si no está duplicada, agrego y aviso.
            #Si ya está, aviso y no agrego.
while True:
    entrada = input("Nombre de la cámara a agregar (o 'fin' para terminar): ")
    
    if entrada.lower() == "fin":
        break
    
    # Evitar duplicados
    if entrada not in lista_camaras:
        lista_camaras.append(entrada)
        print(f"¡Cámara agregada: {entrada}!")
    else:
        print("Esa cámara ya existe.")
        
print("\n--- Lista final de cámaras ---")
for camara in lista_camaras:
    print(f"- {camara}")

print(f"\nTotal de cámaras activas: {len(lista_camaras)}")
# Guardar en archivo
try:
    ruta_salida = Path("inventarios/cctv.txt")
    ruta_salida.parent.mkdir(exist_ok=True)  # crea carpeta si no existe
    with ruta_salida.open("w", encoding="utf-8") as archivo:
        for camara in lista_camaras:
            archivo.write(f"{camara}\n")
    print(f"\n✅ Inventario guardado en: {ruta_salida}")
except Exception as e:
    print(f"❌ Error al guardar: {e}")