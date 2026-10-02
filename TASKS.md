# TASKS — Tareas del Proyecto

## Fase 1: Entorno y Base de Datos
- [x] Inicializar entorno virtual de Python (`venv`).
- [x] Instalar Django y el conector de MySQL (`mysqlclient`).
- [x] Crear la estructura de carpetas (`backend/`, `frontend/`).
- [x] Configurar `settings.py` para usar `asistencia_express` en `127.0.0.1:3308`.
- [x] Crear la base de datos `asistencia_express` en MySQL y comprobar la conexión.

## Fase 2: Modelos (Backend)
- [x] Crear modelos: Curso, Estudiante, Asistencia.
- [x] Ejecutar migraciones.
- [x] Registrar modelos en `admin.py` para cargar datos de prueba.

## Fase 3: Interfaz (Frontend)
- [x] Configurar el sistema de plantillas apuntando a la carpeta `frontend/templates`.
- [x] Crear `base.html` con el navbar, logo Uniguajira, colores institucionales y formato de letra único (Bootstrap).
- [x] Construir la vista de la lista de estudiantes.

## Fase 4: Lógica de 1 Clic
- [x] Crear la vista en Django (View) que recibe la petición de asistencia.
- [x] Escribir el script en JavaScript para capturar el clic y enviar la petición al backend por AJAX.
- [ ] Probar el flujo completo y validar tiempos.

## Fase 5: Estilo del Panel de Administración
- [x] Crear plantilla propia para la portada del admin con accesos a los modelos.
- [x] Aplicar marca Uniguajira, Roboto, paleta institucional y tema claro.
- [x] Traducir la interfaz administrativa al español.
- [x] Revisar la portada en escritorio y móvil; no presenta desbordamiento horizontal en la prueba móvil.
- [x] Ejecutar `python manage.py check` sin errores de configuración.

## Fase 6: Compatibilidad y Validación Integral
- [ ] Resolver la falla de `/admin/asistencia/curso/` observada con Django 4.2.16 y Python 3.14.5 (`Context.__copy__`).
- [ ] Probar listas, formularios de alta/cambio y permisos del admin una vez resuelta la compatibilidad.
- [ ] Crear o cargar datos de prueba: docentes, cursos y estudiantes.
- [ ] Probar que el clic de asistencia persiste el cambio y que la interfaz se sincroniza con la respuesta del servidor.
- [ ] Medir y registrar el tiempo para un grupo de 30 estudiantes; validar el objetivo de menos de 60 segundos.
- [ ] Probar estados de error y verificar que la interfaz permita recuperarse si falla la petición.

## Documentación
- [x] Actualizar estado, decisiones, diseño, requisitos, reporte y reglas con los resultados observados.
- [ ] Reemplazar en `ARCHITECTURE.md` el árbol de referencia por la estructura actual del repositorio.