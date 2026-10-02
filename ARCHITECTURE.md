# ARCHITECTURE — Arquitectura del Proyecto

## Stack Tecnológico Elegido
- **Entorno de Desarrollo:** Visual Studio Code.
- **Backend y Framework:** Python + Django 4.2.16 (rama 4.2 LTS).
- **Runtime detectado:** Python 3.14.5 en el entorno virtual local.
- **Base de Datos:** MySQL / MariaDB 10.4.32 (gestionado vía XAMPP local en puerto 3308, base `asistencia_express`).
- **Frontend (Interfaz):** HTML5, CSS3, JavaScript y Bootstrap 5.

## Estructura de Carpetas de Referencia
El proyecto estará dividido para mantener el orden, todo dentro de un entorno virtual:
```text
sistema_asistencia/
├── venv/                     # Entorno virtual de Python (aislamiento de dependencias)
├── backend/                  # Proyecto Django (Modelos, Vistas, URLs, Configuración)
│   ├── manage.py
│   └── nucleo/               # Aplicación principal de Django
├── frontend/                 # Archivos de interfaz (Templates, CSS, JS, Imágenes)
│   ├── templates/            # Archivos HTML
│   └── static/               # Archivos estáticos (Bootstrap, CSS personalizado, logos)
├── docs/                     # Archivos .md de documentación Vibe Coding
└── .env.example              # Variables de entorno de referencia