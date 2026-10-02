# DECISIONS — Registro de Decisiones Técnicas

## 1. Django como Framework Backend
- **Alternativas:** PHP puro, Node.js.
- **Por qué se elegió:** Django ofrece un ORM robusto y un panel de administración (`/admin`) listo para usar, lo que acelera la gestión de estudiantes y docentes.

## 2. Configuración de MySQL en XAMPP (Puerto 3308)
- **Decisión:** Utilizar el puerto 3308 para MySQL en lugar del 3306.
- **Por qué se eligió:** Previene conflictos con otras instalaciones de bases de datos en la máquina local de desarrollo, asegurando estabilidad.

## 3. Botón de Asistencia de "Un Clic" (AJAX)
- **Alternativas:** Un formulario con checkboxes que se envía recargando toda la página.
- **Por qué se eligió:** Recargar la página toma tiempo y frustra al usuario. Usar JavaScript para enviar el dato de asistencia en segundo plano cumple el criterio de éxito de tomar asistencia en menos de 1 minuto.

## 4. Separación Frontend/Backend
- **Decisión:** Separar los archivos estáticos y plantillas en una carpeta `frontend/` y el código Python en `backend/`.
- **Por qué se eligió:** Mantiene el código ordenado y facilita la escalabilidad y mantenimiento del proyecto.

## 5. Base de datos local del proyecto
- **Decisión:** Usar `asistencia_express` como nombre del schema MySQL del Sistema de Asistencia Express.
- **Por qué se eligió:** El nombre de `DATABASES['default']['NAME']` debe identificar una base de datos del servidor, no una carpeta del proyecto ni una base perteneciente a otro sistema.

## 6. Conector MySQL para Django
- **Decisión:** Usar `mysqlclient` / `pymysql` como conector de base de datos.
- **Por qué se eligió:** Permite una conexión fluida y sin fricción entre Python y el servidor MySQL/MariaDB de XAMPP en Windows.

## 7. Versión de Django (Django 4.2 LTS)
- **Decisión:** Utilizar Django 4.2.16 LTS.
- **Por qué se eligió:** La versión empaquetada por XAMPP es MariaDB 10.4.32. Django 5+ eliminó el soporte para versiones anteriores a MariaDB 10.11 e introdujo sintaxis incompatible (`RETURNING`). Django 4.2 LTS cuenta con soporte nativo y estable para MariaDB 10.4 sin necesidad de parches.

## 8. Personalización del panel de administración
- **Decisión:** Sobrescribir las plantillas base e índice del admin y servir `frontend/static/css/admin.css`.
- **Por qué se eligió:** Reutiliza las funciones CRUD de Django y alinea la portada administrativa con la identidad visual del sitio: Roboto, verde institucional, fondos claros y tarjetas adaptables.
- **Estado:** Implementado. La portada se comprobó en escritorio y móvil; las vistas de listado siguen pendientes por el error descrito en `ARCHITECTURE.md`.

## 9. Idioma de la interfaz
- **Decisión:** Configurar `LANGUAGE_CODE = 'es-co'`.
- **Por qué se eligió:** Mantener el panel y las traducciones del admin en español, coherentes con las plantillas públicas.

## 10. Compatibilidad Python/Django pendiente
- **Estado detectado:** El entorno usa Python 3.14.5 y Django 4.2.16. `manage.py check` pasa, pero la lista de Cursos produce un error dentro de `django.template.context.Context.__copy__`.
- **Pendiente:** Probar y decidir versiones compatibles antes de validar las vistas CRUD, manteniendo la compatibilidad necesaria con MariaDB 10.4.