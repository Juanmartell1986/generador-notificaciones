@echo off
cd /d %~dp0
call venv311\Scripts\activate
python manage.py runserver
pause