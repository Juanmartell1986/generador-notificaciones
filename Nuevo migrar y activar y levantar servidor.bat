@echo off
cd /d %~dp0
echo --- Eliminando base de datos anterior ---
del db.sqlite3

echo --- Eliminando migraciones anteriores ---
rmdir /s /q notificaciones\migrations
mkdir notificaciones\migrations
echo.> notificaciones\migrations\__init__.py

echo --- Activando entorno virtual ---
call venv311\Scripts\activate

echo --- Generando nuevas migraciones ---
python manage.py makemigrations

echo --- Aplicando migraciones ---
python manage.py migrate

echo --- Creando usuario administrador ---
python manage.py shell << EOF
from django.contrib.auth.hashers import make_password
from notificaciones.models import UsuarioPersonal
UsuarioPersonal.objects.create(
    nombre="Administrador",
    correo="jmartellmp@gmail.com",
    clave=make_password("Martell1986"),
    es_admin=True
)
EOF

echo --- Todo listo. 

python manage.py runserver
pause