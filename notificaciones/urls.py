from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista_notificaciones, name='lista_notificaciones'),
    path('generar/', views.generar_notificacion, name='generar_notificacion'),
    path('editar/<int:notificacion_id>/', views.editar_notificacion, name='editar_notificacion'),
    path('citaciones/', views.generar_citaciones, name='generar_citaciones'),
    path('base-datos/', views.base_datos, name='base_datos'),
    path('datos-basicos/', views.datos_basicos, name='datos_basicos'),
    path('registrar-usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('logout/', views.logout_view, name='logout'),
    # User management URLs
    path('usuarios/', views.gestionar_usuarios, name='gestionar_usuarios'),
    path('usuarios/editar/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
]
