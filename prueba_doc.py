from utils.gdocs_generator import generar_cedula_notificacion

plantilla_id = '19bFpAIen4DqR5xPQWNJUUy-YX7_d9xVQPvFddHKC8TI'

datos = {
    "CASO": "2024-000123",
    "NOMBRES": "Juan Martell",
    "URGENCIA": "Alta",
    "DIRECCION": "Av. Justicia 456",
    "DISPOSICION": "5ta Disposición",
    "CONDICION": "Testigo",
    "FISCAL": "Dra. Ramos",
    "FECHA": "25/06/2025"
}

url = generar_cedula_notificacion(datos, plantilla_id)
print("Documento generado:", url)
