@echo off
cd /d %~dp0

echo Activando entorno virtual...
call venv311\Scripts\activate.bat

echo Aplicando migraciones generales...
python manage.py migrate

echo Aplicando migraciones específicas de 'notificaciones'...
python manage.py migrate notificaciones

echo.
echo ✔️ Migraciones completadas. Iniciando servidor...
timeout /t 2 > nul

python manage.py runserver

pause
