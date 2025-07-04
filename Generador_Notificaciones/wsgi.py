"""
WSGI config for Generador_Notificaciones project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Generador_Notificaciones.settings')

application = get_wsgi_application()
