import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Generador_Notificaciones.settings')
django.setup()

from django.contrib.auth.models import User
from notificaciones.models import PerfilUsuario

# Obtener el usuario admin
try:
    admin_user = User.objects.get(username='admin')
    
    # Crear o actualizar el perfil de usuario
    perfil, created = PerfilUsuario.objects.get_or_create(
        user=admin_user,
        defaults={'es_administrador': True}
    )
    
    if created:
        print(f"Perfil de administrador creado para {admin_user.username}")
    else:
        perfil.es_administrador = True
        perfil.save()
        print(f"Perfil de administrador actualizado para {admin_user.username}")
        
except User.DoesNotExist:
    print("Usuario admin no encontrado")
