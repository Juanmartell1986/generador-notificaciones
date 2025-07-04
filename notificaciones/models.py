from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Notificacion(models.Model):
    URGENCIA_CHOICES = [
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    ]
    
    caso = models.CharField(max_length=100, verbose_name='Caso')
    nombres = models.CharField(max_length=200, verbose_name='Nombres')
    urgencia = models.CharField(max_length=10, choices=URGENCIA_CHOICES, verbose_name='Urgencia')
    direccion = models.CharField(max_length=300, verbose_name='Dirección')
    disposicion = models.CharField(max_length=200, verbose_name='Disposición')
    condicion = models.CharField(max_length=100, verbose_name='Condición')
    fiscal = models.CharField(max_length=200, verbose_name='Fiscal')
    fecha = models.DateField(verbose_name='Fecha')
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Creación')
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario Creador')
    documento_url = models.URLField(blank=True, null=True, verbose_name='URL del Documento')
    
    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.caso} - {self.nombres}"

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    es_administrador = models.BooleanField(default=False, verbose_name='Es Administrador')
    fecha_registro = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Registro')
    
    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuario'
    
    def __str__(self):
        return f"{self.user.username} - {'Admin' if self.es_administrador else 'Usuario'}"
