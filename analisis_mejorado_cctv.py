#pandas → Panel Data Analysis
import pandas as pd
#aqui van las listas de las camaras
# Descripcion completa de las camaras del edificio B3
CCTV_edificio_B3 = {
#todo el edificio
    "B3_NVR": [
# el primer grabador
        {
            "id": "camara_001",
            "nombre": "camara_de_entrada_001",
            "ubicacion": "entrada_principal",
            "ip": "192.168.1.105",
            "estado": "operativa",
            "resolucion": "720p",
            "tecnologia": "tvl"
        },
        {
            "id": "camara_002",
            "nombre": "camara_de_entrada_002",
            "ubicacion": "entrada_principal",
            "ip": "192.168.1.106",
            "estado": "operativa",
            "resolucion": "4k",
            "tecnologia": "digital"
        },
        {
            "id": "camara_003",
            "nombre": "camara_de_entrada_003",
            "ubicacion": "entrada_principal",
            "ip": "192.168.1.108",
            "estado": "operativa",
            "resolucion": "4k",
            "tecnologia": "digital"
        },
        {
            "id": "camara_004",
            "nombre": "camara_de_estacionamiento_001",
            "ubicacion": "estacionamiento",
            "ip": "192.168.1.107",
            "estado": "operativa",
            "resolucion": "vga",
            "tecnologia": "analoga"
        },
        {
            "id": "camara_005",
            "nombre": "camara_de_estacionamiento_002",
            "ubicacion": "estacionamiento",
            "ip": "192.168.1.110",
            "estado": "operativa",
            "resolucion": "8k",
            "tecnologia": "ptz"
        },
        {
            "id": "camara_006",
            "nombre": "camara_de_pasillo",
            "ubicacion": "pasillo",
            "ip": "192.168.1.111",
            "estado": "operativa",
            "resolucion": "1080p",
            "tecnologia": "digital"
        },
        {
            "id": "camara_007",
            "nombre": "escalera_001",
            "ubicacion": "escalera",
            "ip": "192.168.1.112",
            "estado": "danada",
            "resolucion": "1080p",
            "tecnologia": "digital"
        },
        {
            "id": "camara_008",
            "nombre": "escalera_002",
            "ubicacion": "escalera",
            "ip": "192.168.1.117",
            "estado": "operativa",
            "resolucion": "720p",
            "tecnologia": "tvl"
        },
        {
            "id": "camara_009",
            "nombre": "techo",
            "ubicacion": "techo",
            "ip": "192.168.1.116",
            "estado": "operativa",
            "resolucion": "4k",
            "tecnologia": "ptz"
        },
        {
            "id": "camara_010",
            "nombre": "cuarto_de_lavado",
            "ubicacion": "cuarto_de_lavado_y_balcon",
            "ip": "192.168.1.119",
            "estado": "operativa",
            "resolucion": "2k",
            "tecnologia": "ptz"
        },
        {
            "id": "camara_011",
            "nombre": "pasillo_2_piso",
            "ubicacion": "pasillo_del_segundo_piso",
            "ip": "192.168.1.122",
            "estado": "operativa",
            "resolucion": "1080p",
            "tecnologia": "digital"
        },
        {
            "id": "camara_012",
            "nombre": "camara_de_recepcion",
            "ubicacion": "recepcion",
            "ip": "192.168.1.123",
            "estado": "operativa",
            "resolucion": "1080p",
            "tecnologia": "digital"
        },
        {
            "id": "camara_013",
            "nombre": "patio_trasero_001",
            "ubicacion": "patio_trasero",
            "ip": "192.168.1.124",
            "estado": "fuera_de_servicio",
            "resolucion": "720p",
            "tecnologia": "tvl"
        },
        {
            "id": "camara_014",
            "nombre": "estacionamiento_003",
            "ubicacion": "estacionamiento",
            "ip": "192.168.1.125",
            "estado": "operativa",
            "resolucion": "4k",
            "tecnologia": "ptz"
        },
        {
            "id": "camara_015",
            "nombre": "entrada_secundaria",
            "ubicacion": "entrada_secundaria",
            "ip": "192.168.1.126",
            "estado": "operativa",
            "resolucion": "2k",
            "tecnologia": "digital"
        },
        {
            "id": "camara_016",
            "nombre": "bodega_001",
            "ubicacion": "bodega",
            "ip": "192.168.1.127",
            "estado": "danada",
            "resolucion": "vga",
            "tecnologia": "analoga"
        }
    ],
# el segundo grabador
    "B3_DVR_1": [
        {
            "id": "camara_017",
            "nombre": "cuarto_de_servidores",
            "ubicacion": "cuarto_de_servidores",
            "ip": "192.168.1.128",
            "estado": "operativa",
            "resolucion": "8k",
            "tecnologia": "digital"
        },
        {
            "id": "camara_018",
            "nombre": "pasillo_3_piso",
            "ubicacion": "pasillo_del_tercer_piso",
            "ip": "192.168.1.129",
            "estado": "operativa",
            "resolucion": "1080p",
            "tecnologia": "digital"
        },
        {
            "id": "camara_019",
            "nombre": "comedor",
            "ubicacion": "area_de_comedor",
            "ip": "192.168.1.130",
            "estado": "operativa",
            "resolucion": "720p",
            "tecnologia": "tvl"
        },
        {
            "id": "camara_020",
            "nombre": "ascensor_001",
            "ubicacion": "ascensor",
            "ip": "192.168.1.131",
            "estado": "fuera_de_servicio",
            "resolucion": "vga",
            "tecnologia": "analoga"
        },
        {
            "id": "camara_021",
            "nombre": "sala_de_juntas",
            "ubicacion": "sala_de_juntas",
            "ip": "192.168.1.132",
            "estado": "operativa",
            "resolucion": "4k",
            "tecnologia": "ptz"
        },
        {
            "id": "camara_022",
            "nombre": "garaje_interno",
            "ubicacion": "garaje_interno",
            "ip": "192.168.1.133",
            "estado": "operativa",
            "resolucion": "1080p",
            "tecnologia": "digital"
        },
        {
            "id": "camara_023",
            "nombre": "terraza",
            "ubicacion": "terraza",
            "ip": "192.168.1.134",
            "estado": "operativa",
            "resolucion": "2k",
            "tecnologia": "ptz"
        },
        {
            "id": "camara_024",
            "nombre": "cuarto_de_basura",
            "ubicacion": "cuarto_de_basura",
            "ip": "192.168.1.135",
            "estado": "danada",
            "resolucion": "720p",
            "tecnologia": "tvl"
        },
        {
            "id": "camara_025",
            "nombre": "entrada_de_carga",
            "ubicacion": "entrada_de_carga",
            "ip": "192.168.1.136",
            "estado": "operativa",
            "resolucion": "4k",
            "tecnologia": "digital"
        },
        {
            "id": "camara_026",
            "nombre": "hall_principal",
            "ubicacion": "hall_principal",
            "ip": "192.168.1.137",
            "estado": "operativa",
            "resolucion": "1080p",
            "tecnologia": "digital"
        },
        {
            "id": "camara_027",
            "nombre": "jardin_delantero",
            "ubicacion": "jardin_delantero",
            "ip": "192.168.1.138",
            "estado": "fuera_de_servicio",
            "resolucion": "vga",
            "tecnologia": "analoga"
        },
        {
            "id": "camara_028",
            "nombre": "cocina",
            "ubicacion": "cocina",
            "ip": "192.168.1.139",
            "estado": "operativa",
            "resolucion": "2k",
            "tecnologia": "ptz"
        },
        {
            "id": "camara_029",
            "nombre": "biblioteca",
            "ubicacion": "biblioteca",
            "ip": "192.168.1.140",
            "estado": "operativa",
            "resolucion": "1080p",
            "tecnologia": "digital"
        },
        {
            "id": "camara_030",
            "nombre": "cancha_deportiva",
            "ubicacion": "area_deportiva",
            "ip": "192.168.1.141",
            "estado": "operativa",
            "resolucion": "8k",
            "tecnologia": "ptz"
        },
        {
            "id": "camara_031",
            "nombre": "puerta_trasera",
            "ubicacion": "puerta_trasera",
            "ip": "192.168.1.142",
            "estado": "danada",
            "resolucion": "720p",
            "tecnologia": "tvl"
        },
        {
            "id": "camara_032",
            "nombre": "sala_de_monitoreo",
            "ubicacion": "sala_de_monitoreo",
            "ip": "192.168.1.143",
            "estado": "operativa",
            "resolucion": "4k",
            "tecnologia": "digital"
        }
    ],
# el tercer grabador
    "B3_DVR_2": [
        {
            "id": "camara_033",
            "nombre": "cubiculo_administrativo",
            "ubicacion": "cubiculos_administrativos",
            "ip": "192.168.1.144",
            "estado": "operativa",
            "resolucion": "1080p",
            "tecnologia": "digital"
        },
        {
            "id": "camara_034",
            "nombre": "salida_emergencia_2",
            "ubicacion": "salida_de_emergencia_segundo_piso",
            "ip": "192.168.1.145",
            "estado": "danada",
            "resolucion": "720p",
            "tecnologia": "tvl"
        },
        {
            "id": "camara_035",
            "nombre": "estacionamiento_subterraneo",
            "ubicacion": "estacionamiento_subterraneo",
            "ip": "192.168.1.146",
            "estado": "operativa",
            "resolucion": "4k",
            "tecnologia": "ptz"
        },
        {
            "id": "camara_036",
            "nombre": "vestidores",
            "ubicacion": "area_de_vestidores",
            "ip": "192.168.1.147",
            "estado": "fuera_de_servicio",
            "resolucion": "vga",
            "tecnologia": "analoga"
        },
        {
            "id": "camara_037",
            "nombre": "cuarto_de_maquinas",
            "ubicacion": "cuarto_de_maquinas",
            "ip": "192.168.1.148",
            "estado": "operativa",
            "resolucion": "2k",
            "tecnologia": "digital"
        },
        {
            "id": "camara_038",
            "nombre": "mirador",
            "ubicacion": "mirador",
            "ip": "192.168.1.149",
            "estado": "operativa",
            "resolucion": "8k",
            "tecnologia": "ptz"
        },
        {
            "id": "camara_039",
            "nombre": "pasillo_basement",
            "ubicacion": "pasillo_del_sotano",
            "ip": "192.168.1.150",
            "estado": "danada",
            "resolucion": "720p",
            "tecnologia": "tvl"
        },
        {
            "id": "camara_040",
            "nombre": "entrada_de_personal",
            "ubicacion": "entrada_de_personal",
            "ip": "192.168.1.151",
            "estado": "operativa",
            "resolucion": "1080p",
            "tecnologia": "digital"
        }
    ]
}

# Cálculo y visualización del total de cámaras
total_camaras = (
    len(CCTV_edificio_B3["B3_NVR"])
    + len(CCTV_edificio_B3["B3_DVR_1"])
    + len(CCTV_edificio_B3["B3_DVR_2"])
)

print(f"Total de camaras del edificio B3: {total_camaras}")
print(f"Camaras en NVR: {len(CCTV_edificio_B3['B3_NVR'])}")
print(f"Camaras en DVR 1: {len(CCTV_edificio_B3['B3_DVR_1'])}")
print(f"Camaras en DVR 2: {len(CCTV_edificio_B3['B3_DVR_2'])}")

# 3. Aplanar los datos: de diccionario anidado → lista plana
datos_para_pandas = []
for grabador, camaras in CCTV_edificio_B3.items():
    for cam in camaras:
        cam["grabador"] = grabador  # Añadir columna 'grabador'
        datos_para_pandas.append(cam)

# 4. ✅ ¡Crear tu primer DataFrame profesional!
df_cctv = pd.DataFrame(datos_para_pandas)

print("✅ DataFrame creado con éxito!")
print(f"📊 {len(df_cctv)} cámaras cargadas")
print(f"📋 Columnas: {list(df_cctv.columns)}")

print("\n" + "="*50)
print("🔍 VISTA RÁPIDA: Primer vistazo al sistema")
print("="*50)

# 1. Primeras 5 cámaras (como revisar las primeras filas del reporte)
print("📌 Primeras 5 cámaras:")
print(df_cctv.head())

# 2. Información técnica (como revisar especificaciones del sistema)
print("\n📋 Información del DataFrame:")
print(df_cctv.info())

# 3. Estadísticas descriptivas (resumen ejecutivo)
print("\n📈 Estadísticas rápidas:")
print(df_cctv.describe(include='all').T)  # .T = transponer → más legible


# ================================
# PASO 3: FILTRADO AVANZADO — Cámaras dañadas
# ================================
print("\n" + "="*50)
print("🚨 CÁMARAS DAÑADAS — Reporte para mantenimiento")
print("="*50)

# Filtrar en 1 línea (vs 5+ en Python puro)
df_danadas = df_cctv[df_cctv["estado"] == "danada"]

print(f"❌ Cámaras dañadas: {len(df_danadas)}")
print("\n📋 Detalle:")
# Mostrar solo columnas relevantes para mantenimiento
print(df_danadas[["id", "nombre", "ubicacion", "grabador", "tecnologia"]].to_string(index=False))

# ================================
# PASO 4: AGRUPACIÓN — Reporte por grabador y estado
# ================================
print("\n" + "="*50)
print("📊 REPORTE: Cámaras por grabador y estado")
print("="*50)

# Tabla pivot: fácil lectura para jefatura
pivot = df_cctv.pivot_table(
    index="grabador",
    columns="estado",
    values="id",
    aggfunc="count",
    fill_value=0
)
print(pivot)

# ================================
# PASO 5: EXPORTACIÓN — Guardar reporte para mantenimiento
# ================================
print("\n" + "="*50)
print("💾 EXPORTACIÓN: Reporte de cámaras dañadas")
print("="*50)

# Guardar en CSV (listo para imprimir/enviar)
df_danadas.to_csv("reporte_camaras_danadas.csv", index=False)
print("✅ Reporte guardado: 'reporte_camaras_danadas.csv'")
print("📁 Archivo listo en: C:\\MLS\\mlops\\reporte_camaras_danadas.csv")

