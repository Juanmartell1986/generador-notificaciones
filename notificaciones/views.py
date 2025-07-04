from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import NotificacionForm, UserEditForm
from .models import Notificacion, PerfilUsuario
from utils.gdocs_generator import generar_cedula_notificacion
from datetime import datetime

@login_required
def lista_notificaciones(request):
    notificaciones = Notificacion.objects.all()
    usuarios = User.objects.all().select_related('perfilusuario')
    
    return render(request, 'notificaciones/lista_notificaciones.html', {
        'notificaciones': notificaciones,
        'usuarios': usuarios,
    })

@login_required
def generar_notificacion(request):
    if request.method == 'POST':
        form = NotificacionForm(request.POST)
        if form.is_valid():
            try:
                # Preparar los datos para el generador
                datos = {
                    "CASO": form.cleaned_data['caso'],
                    "NOMBRES": form.cleaned_data['nombres'],
                    "URGENCIA": form.cleaned_data['urgencia'],
                    "DIRECCION": form.cleaned_data['direccion'],
                    "DISPOSICION": form.cleaned_data['disposicion'],
                    "CONDICION": form.cleaned_data['condicion'],
                    "FISCAL": form.cleaned_data['fiscal'],
                    "FECHA": form.cleaned_data['fecha'].strftime("%d/%m/%Y")
                }
                
                # ID de la plantilla de Google Docs
                plantilla_id = '19bFpAIen4DqR5xPQWNJUUy-YX7_d9xVQPvFddHKC8TI'
                
                # Generar el documento
                url = generar_cedula_notificacion(datos, plantilla_id)
                
                # Guardar la notificación en la base de datos
                notificacion = Notificacion(
                    caso=form.cleaned_data['caso'],
                    nombres=form.cleaned_data['nombres'],
                    urgencia=form.cleaned_data['urgencia'],
                    direccion=form.cleaned_data['direccion'],
                    disposicion=form.cleaned_data['disposicion'],
                    condicion=form.cleaned_data['condicion'],
                    fiscal=form.cleaned_data['fiscal'],
                    fecha=form.cleaned_data['fecha'],
                    usuario_creador=request.user,
                    documento_url=url
                )
                notificacion.save()
                
                # Mostrar mensaje de éxito con el enlace
                messages.success(
                    request,
                    f'Documento generado exitosamente. <a href="{url}" target="_blank">Ver documento</a>',
                    extra_tags='safe'
                )
                return redirect('lista_notificaciones')
                
            except Exception as e:
                messages.error(request, f'Error al generar el documento: {str(e)}')
    else:
        form = NotificacionForm()
    
    return render(request, 'notificaciones/generar_notificacion.html', {
        'form': form,
        'titulo': 'Generar Cédula de Notificación'
    })

@login_required
def editar_notificacion(request, notificacion_id):
    notificacion = get_object_or_404(Notificacion, id=notificacion_id)
    
    if request.method == 'POST':
        form = NotificacionForm(request.POST)
        if form.is_valid():
            # Actualizar los datos de la notificación
            notificacion.caso = form.cleaned_data['caso']
            notificacion.nombres = form.cleaned_data['nombres']
            notificacion.urgencia = form.cleaned_data['urgencia']
            notificacion.direccion = form.cleaned_data['direccion']
            notificacion.disposicion = form.cleaned_data['disposicion']
            notificacion.condicion = form.cleaned_data['condicion']
            notificacion.fiscal = form.cleaned_data['fiscal']
            notificacion.fecha = form.cleaned_data['fecha']
            notificacion.save()
            
            messages.success(request, 'Notificación actualizada exitosamente.')
            return redirect('lista_notificaciones')
    else:
        # Prellenar el formulario con los datos existentes
        form = NotificacionForm(initial={
            'caso': notificacion.caso,
            'nombres': notificacion.nombres,
            'urgencia': notificacion.urgencia,
            'direccion': notificacion.direccion,
            'disposicion': notificacion.disposicion,
            'condicion': notificacion.condicion,
            'fiscal': notificacion.fiscal,
            'fecha': notificacion.fecha,
        })
    
    return render(request, 'notificaciones/generar_notificacion.html', {
        'form': form,
        'titulo': 'Editar Notificación',
        'editando': True,
        'notificacion': notificacion
    })

@login_required
def generar_citaciones(request):
    return render(request, 'notificaciones/en_construccion.html', {
        'titulo': 'Generar Citaciones',
        'mensaje': 'Esta funcionalidad está en construcción.'
    })

@login_required
def base_datos(request):
    return render(request, 'notificaciones/en_construccion.html', {
        'titulo': 'Base de Datos',
        'mensaje': 'Esta funcionalidad está en construcción.'
    })

@login_required
def datos_basicos(request):
    return render(request, 'notificaciones/en_construccion.html', {
        'titulo': 'Datos Básicos',
        'mensaje': 'Esta funcionalidad está en construcción.'
    })

@login_required
def registrar_usuario(request):
    # Solo administradores pueden registrar usuarios
    if not hasattr(request.user, 'perfilusuario') or not request.user.perfilusuario.es_administrador:
        messages.error(request, 'No tiene permisos para acceder a esta sección.')
        return redirect('lista_notificaciones')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear perfil de usuario
            PerfilUsuario.objects.create(user=user, es_administrador=False)
            messages.success(request, f'Usuario {user.username} creado exitosamente.')
            return redirect('lista_notificaciones')
    else:
        form = UserCreationForm()
    
    return render(request, 'notificaciones/registrar_usuario.html', {
        'form': form,
        'titulo': 'Registrar Nuevo Usuario'
    })

def home(request):
    if request.user.is_authenticated:
        return redirect('lista_notificaciones')
    else:
        return redirect('login')

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')

def es_administrador(user):
    return hasattr(user, 'perfilusuario') and user.perfilusuario.es_administrador

@login_required
@user_passes_test(es_administrador)
def gestionar_usuarios(request):
    users = User.objects.all().select_related('perfilusuario')
    return render(request, 'notificaciones/gestionar_usuarios.html', {
        'users': users
    })

@login_required
@user_passes_test(es_administrador)
def editar_usuario(request, user_id):
    edit_user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=edit_user)
        if form.is_valid():
            user = form.save()
            # Actualizar el estado de administrador
            perfil = user.perfilusuario
            perfil.es_administrador = form.cleaned_data['es_administrador']
            perfil.save()
            
            messages.success(request, f'Usuario {user.username} actualizado exitosamente.')
            return redirect('gestionar_usuarios')
    else:
        form = UserEditForm(
            instance=edit_user,
            initial={'es_administrador': edit_user.perfilusuario.es_administrador}
        )
    
    return render(request, 'notificaciones/editar_usuario.html', {
        'form': form,
        'edit_user': edit_user
    })
