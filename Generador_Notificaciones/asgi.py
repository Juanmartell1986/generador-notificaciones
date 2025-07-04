"""
ASGI config for Generador_Notificaciones project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Generador_Notificaciones.settings')

application = get_asgi_application()
