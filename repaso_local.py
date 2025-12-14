from pathlib import Path

print("=== INICIO REPASO ===")

ruta = Path("repaso.txt")

if ruta.exists():
    contenido = ruta.read_text()
    print("Archivo encontrado")
    print("Contenido:")
    print(contenido)
else:
    print("Archivo NO encontrado")
    print("Se creará uno nuevo")

    ruta.write_text("Este archivo fue creado por repaso_local.py\n")
    print("Archivo creado correctamente")

print("=== FIN REPASO ===")
