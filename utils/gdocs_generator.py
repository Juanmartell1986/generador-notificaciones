from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import os

def generar_cedula_notificacion(datos, plantilla_id):
    """
    Genera una cédula de notificación usando Google Docs
    
    Args:
        datos (dict): Diccionario con los datos a reemplazar en la plantilla
        plantilla_id (str): ID del documento de Google Docs que sirve como plantilla
    
    Returns:
        str: URL del documento generado
    """
    try:
        # Cargar las credenciales desde el archivo JSON
        credentials = service_account.Credentials.from_service_account_file(
            'serviceAccountKey.json',
            scopes=['https://www.googleapis.com/auth/documents']
        )

        # Crear el servicio de Google Docs
        service = build('docs', 'v1', credentials=credentials)

        # Crear una copia del documento plantilla
        body = {
            'name': f'Cédula de Notificación - {datos["CASO"]}'
        }
        drive_service = build('drive', 'v3', credentials=credentials)
        documento = drive_service.files().copy(
            fileId=plantilla_id,
            body=body
        ).execute()

        # Preparar las solicitudes de reemplazo
        requests = []
        for key, value in datos.items():
            requests.append({
                'replaceAllText': {
                    'containsText': {
                        'text': f'{{{key}}}',
                        'matchCase': True
                    },
                    'replaceText': str(value)
                }
            })

        # Ejecutar las solicitudes de reemplazo
        service.documents().batchUpdate(
            documentId=documento['id'],
            body={'requests': requests}
        ).execute()

        # Retornar la URL del documento
        return f"https://docs.google.com/document/d/{documento['id']}/edit"

    except Exception as e:
        raise Exception(f"Error al generar el documento: {str(e)}")
