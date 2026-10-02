# REPORTE DE AVANCE — Sistema de Asistencia Express (Uniguajira)

**Desarrollador:** jesus silva montalvo
**Fecha:** Octubre 2026

## 1. Resumen Ejecutivo
Se implementó la base de una aplicación web para agilizar el llamado a lista, separando backend y frontend y conectando Django con una base de datos relacional. La validación integral del MVP continúa pendiente.

## 2. Arquitectura y Tecnologías
- **Backend:** Python 3.14.5 y Django 4.2.16 detectados en el entorno local; ORM de Django para los modelos y la lógica de negocio.
- **Base de Datos:** MySQL ejecutado a través de XAMPP local en el puerto 3308 para evitar conflictos de red.
- **Frontend:** Construido con HTML5, JavaScript y Bootstrap 5, garantizando un diseño responsivo (Mobile-first).

## 3. Identidad Visual y UX
- Se respetó estrictamente la paleta de colores institucional de la Universidad de La Guajira (Verde, Blanco y Negro).
- Se implementó una única familia tipográfica (Roboto) para mantener la coherencia visual.
- **Innovación en UX (Un solo clic):** Se integró tecnología AJAX (JavaScript) para que al hacer clic en el botón de asistencia, el estado se guarde en la base de datos en segundo plano sin recargar la página, cumpliendo el requisito de máxima velocidad.

## 4. Estructura de Datos
Se implementaron los siguientes modelos principales en la base de datos MySQL:
1. **Docente:** (Autenticación nativa de Django).
2. **Curso:** Relacionado al docente responsable.
3. **Estudiante:** Con su respectivo código estudiantil.
4. **Asistencia:** Tabla transaccional que registra la fecha exacta y el estado (Falta/Asistencia) mediante una relación con el estudiante y el curso.

## 5. Conclusiones
- La implementación del endpoint y la interfaz AJAX está hecha, pero todavía no se ha documentado una prueba integral ni una medición para 30 estudiantes.
- La portada del admin fue personalizada con plantillas Django y CSS institucional, traducida al español y revisada en escritorio y móvil.
- `python manage.py check` no reporta problemas de configuración.

## 6. Validación pendiente
- Al abrir `/admin/asistencia/curso/`, Django 4.2.16 produce un error en `django.template.context.Context.__copy__` con Python 3.14.5. Las listas y formularios CRUD no están validados hasta resolver y probar la compatibilidad.
- Falta cargar datos de prueba y verificar persistencia, actualización visual, manejo de errores y el criterio de menos de 60 segundos para 30 estudiantes.
- Por lo anterior, el objetivo de éxito del `PRD.md` todavía no puede reportarse como cumplido.