# MEMORIA DEL PROYECTO - GENERADOR DE NOTIFICACIONES

## 1. ANÁLISIS DEL PROYECTO

### Descripción General
El proyecto "Generador_Notificaciones" es una aplicación web Django que permite generar cédulas de notificación utilizando plantillas de Google Docs. La aplicación integra la API de Google Docs para automatizar la creación de documentos legales con datos específicos.

### Tecnologías Utilizadas
- **Backend**: Django 5.2.4
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.0
- **Base de Datos**: SQLite3
- **APIs Externas**: Google Docs API, Google Drive API
- **Autenticación**: Google Service Account
- **Fuentes**: Google Fonts (Inter)
- **Lenguaje**: Python 3.10+

## 2. ESTRUCTURA DEL PROYECTO

```
/project/sandbox/user-workspace/
├── manage.py                           # Comando principal de Django
├── db.sqlite3                         # Base de datos SQLite
├── serviceAccountKey.json             # Credenciales de Google API
├── prueba_doc.py                      # Script de prueba para generación de documentos
├── qr_temp.png                        # Imagen temporal de QR
├── 
├── Generador_Notificaciones/          # Configuración principal del proyecto
│   ├── __init__.py
│   ├── settings.py                    # Configuraciones de Django
│   ├── urls.py                        # URLs principales
│   ├── wsgi.py                        # Configuración WSGI
│   └── asgi.py                        # Configuración ASGI
├── 
├── notificaciones/                    # Aplicación principal
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── forms.py                       # Formularios Django
│   ├── views.py                       # Vistas de la aplicación
│   ├── urls.py                        # URLs de la aplicación
│   └── templates/notificaciones/
│       └── generar_notificacion.html  # Plantilla principal
├── 
├── utils/                             # Utilidades del proyecto
│   └── gdocs_generator.py             # Generador de documentos Google Docs
├── 
└── Archivos batch (Windows):
    ├── aplicar_migraciones.bat
    ├── forzar_migraciones.bat
    ├── iniciar_django.bat
    ├── iniciar_servidor.bat
    └── Nuevo migrar y activar y levantar servidor.bat
```

## 3. FUNCIONALIDADES IMPLEMENTADAS

### 3.1 Generación de Documentos
- **Función**: `generar_cedula_notificacion()` en `utils/gdocs_generator.py`
- **Propósito**: Crear documentos de notificación basados en plantillas de Google Docs
- **Parámetros**:
  - `datos`: Diccionario con información del caso
  - `plantilla_id`: ID del documento de Google Docs usado como plantilla

### 3.2 Formulario Web
- **Campos del formulario**:
  - Caso (obligatorio)
  - Nombres (obligatorio)
  - Urgencia (Alta/Media/Baja)
  - Dirección (obligatorio)
  - Disposición (obligatorio)
  - Condición (obligatorio)
  - Fiscal (obligatorio)
  - Fecha (obligatorio)

### 3.3 Interfaz de Usuario
- **Diseño**: Moderno con colores negro y blanco
- **Framework CSS**: Bootstrap 5.3.0
- **Tipografía**: Google Fonts (Inter)
- **Responsivo**: Adaptable a diferentes dispositivos
- **Validación**: Mensajes de error en tiempo real

### 3.4 Integración con Google APIs
- **Autenticación**: Service Account con archivo JSON
- **Servicios utilizados**:
  - Google Docs API v1
  - Google Drive API v3
- **Funcionalidades**:
  - Copia de plantillas
  - Reemplazo de texto en documentos
  - Generación de URLs de acceso

## 4. CONFIGURACIÓN ACTUAL

### 4.1 Settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notificaciones',  # Aplicación principal
]

ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1', 'w8pd4s-8000.csb.app']
LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
```

### 4.2 Dependencias Instaladas
```
django==5.2.4
google-api-python-client==2.175.0
google-auth-httplib2==0.2.0
google-auth-oauthlib==1.2.2
```

## 5. DATOS DE PRUEBA

### Ejemplo de datos utilizados en prueba_doc.py:
```python
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
```

### ID de plantilla de Google Docs:
```
plantilla_id = '19bFpAIen4DqR5xPQWNJUUy-YX7_d9xVQPvFddHKC8TI'
```

## 6. PRÓXIMOS PASOS PARA EL DESARROLLO

### 6.1 Mejoras Inmediatas
1. **Validación del archivo serviceAccountKey.json**
   - Verificar que el archivo existe y es válido
   - Implementar manejo de errores específicos

2. **Mejora del formulario**
   - Agregar validación JavaScript del lado cliente
   - Implementar autocompletado para campos comunes
   - Agregar campo de observaciones opcional

3. **Historial de documentos**
   - Crear modelo para almacenar historial de generaciones
   - Implementar vista para consultar documentos anteriores
   - Agregar funcionalidad de búsqueda

### 6.2 Funcionalidades Avanzadas
1. **Autenticación de usuarios**
   - Sistema de login/logout
   - Perfiles de usuario con permisos
   - Auditoría de acciones

2. **Múltiples plantillas**
   - Soporte para diferentes tipos de notificaciones
   - Gestión de plantillas desde la interfaz web
   - Previsualización de plantillas

3. **Exportación adicional**
   - Generación de PDFs
   - Envío por correo electrónico
   - Integración con sistemas de gestión documental

### 6.3 Optimizaciones
1. **Performance**
   - Cache de plantillas frecuentemente usadas
   - Optimización de consultas a la API de Google
   - Implementación de tareas asíncronas

2. **Seguridad**
   - Validación estricta de datos de entrada
   - Sanitización de contenido
   - Implementación de CSRF tokens

## 7. COMANDOS ÚTILES

### Desarrollo
```bash
# Iniciar servidor de desarrollo
python manage.py runserver 0.0.0.0:8000

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Verificar configuración
python manage.py check
```

### Pruebas
```bash
# Ejecutar pruebas
python manage.py test

# Ejecutar script de prueba
python prueba_doc.py
```

## 8. SOLUCIÓN DE PROBLEMAS COMUNES

### 8.1 Error de Google API
**Problema**: "Error al generar el documento"
**Solución**: 
- Verificar que serviceAccountKey.json existe
- Comprobar permisos del Service Account
- Validar que la plantilla de Google Docs es accesible

### 8.2 Error de ALLOWED_HOSTS
**Problema**: "Invalid HTTP_HOST header"
**Solución**: Agregar el host al setting ALLOWED_HOSTS

### 8.3 Error de dependencias
**Problema**: "ModuleNotFoundError"
**Solución**: 
```bash
pip install django google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## 9. NOTAS DE DESARROLLO

### 9.1 Consideraciones de Seguridad
- El archivo serviceAccountKey.json contiene credenciales sensibles
- No debe ser incluido en control de versiones
- Debe ser protegido con permisos restrictivos

### 9.2 Escalabilidad
- La aplicación actual está diseñada para uso interno
- Para producción, considerar:
  - Base de datos PostgreSQL
  - Servidor web Nginx + Gunicorn
  - Variables de entorno para configuración

### 9.3 Mantenimiento
- Revisar periódicamente las credenciales de Google API
- Actualizar dependencias regularmente
- Monitorear logs de errores

## 10. CONTACTO Y DOCUMENTACIÓN

### Recursos Adicionales
- [Documentación de Django](https://docs.djangoproject.com/)
- [Google Docs API](https://developers.google.com/docs/api)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

### Estructura de Archivos de Configuración
- `settings.py`: Configuración principal de Django
- `urls.py`: Enrutamiento de URLs
- `forms.py`: Definición de formularios
- `views.py`: Lógica de vistas
- `gdocs_generator.py`: Integración con Google APIs

---

**Última actualización**: 04 de Julio de 2025
**Versión del proyecto**: 1.0.0
**Estado**: En desarrollo activo
