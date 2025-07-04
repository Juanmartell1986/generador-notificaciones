from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NotificacionForm(forms.Form):
    caso = forms.CharField(
        label='Caso',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nombres = forms.CharField(
        label='Nombres',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    urgencia = forms.ChoiceField(
        label='Urgencia',
        choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    direccion = forms.CharField(
        label='Dirección',
        max_length=300,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    disposicion = forms.CharField(
        label='Disposición',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    condicion = forms.CharField(
        label='Condición',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fiscal = forms.CharField(
        label='Fiscal',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fecha = forms.DateField(
        label='Fecha',
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        )
    )

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nombres',
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Apellidos',
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Correo electrónico',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    es_administrador = forms.BooleanField(
        label='Es administrador',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
