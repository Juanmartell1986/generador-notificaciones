@echo off
cd /d C:\Users\JM\Generador_Notificaciones
echo Activando entorno virtual...
call venv311\Scripts\activate

echo Forzando migraciones...
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo Listo. Iniciando servidor...
python manage.py runserver

pause
