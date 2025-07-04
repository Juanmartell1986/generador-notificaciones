
Built by https://www.blackbox.ai

---

# Generador de Notificaciones

## Project Overview
The **Generador de Notificaciones** is a Django web application designed to automate the generation of legal notification documents using Google Docs templates. It integrates the Google Docs API to create documents with specific data, streamlining the process of legal documentation.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/generador_notificaciones.git
    cd generador_notificaciones
    ```

2. **Create a virtual environment** (optional, but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Django and other dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup Google API credentials**:
   - Create a service account in Google Cloud and download the `serviceAccountKey.json` file. Place it in the project root directory.

5. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser** (optional, for admin panel access):
    ```bash
    python manage.py createsuperuser
    ```

## Usage

To start the application, run the following command:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application. You can use the `/prueba_doc.py` script to test the generation of notification documents based on predefined data.

## Features

- **Document Generation**: Automatically create legal notification documents using Google Docs templates.
- **User-Friendly Forms**: Input forms for easy data entry, complete with real-time validation.
- **Responsive Design**: A modern web interface that adapts to various devices using Bootstrap 5.3.0.
- **Google API Integration**: Utilizes the Google Docs and Drive API for document creation and management.

## Dependencies

The project dependencies can be found in the `requirements.txt` file or `settings.py`. Key dependencies include:

- `django==5.2.4`
- `google-api-python-client==2.175.0`
- `google-auth-httplib2==0.2.0`
- `google-auth-oauthlib==1.2.2`

## Project Structure

Here is a brief overview of the project structure:

```
/Generador_Notificaciones/
├── manage.py                           # Main Django command-line utility
├── db.sqlite3                         # SQLite database
├── serviceAccountKey.json             # Google API credentials
├── prueba_doc.py                      # Script for testing document generation
├── Generador_Notificaciones/          # Main project folder
│   ├── __init__.py
│   ├── settings.py                    # Django settings configuration
│   ├── urls.py                        # URL routing
│   ├── wsgi.py                        # WSGI configuration
│   └── asgi.py                        # ASGI configuration
│   
├── notificaciones/                    # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── forms.py                       # Django forms
│   ├── views.py                       # Application views
│   ├── urls.py                        # Application URLs
│   └── templates/notificaciones/
│       └── generar_notificacion.html  # Main template
│   
└── utils/                             # Project utilities
    └── gdocs_generator.py             # Google Docs document generator
```

This structured approach to organizing files facilitates maintainability and scalability.

### Additional Notes

Make sure to secure the `serviceAccountKey.json` file and avoid exposing it in public repositories. For development, consider using a `.env` file to manage sensitive settings and configurations. 

**Project Status**: In active development.