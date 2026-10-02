# MEMORY — Estado Actual del Proyecto

## Estado actual
- ✅ **Fase 1 completada:** Entorno virtual, Django 4.2.16, MySQL/MariaDB `asistencia_express` en el puerto 3308 y migración inicial configurados.
- ✅ **Fase 2 completada:** Modelos `Curso`, `Estudiante` y `Asistencia` creados y registrados en el admin.
- ✅ **Fase 3 completada:** Lista pública con Bootstrap 5, identidad Uniguajira, Roboto y asistencia de un clic implementada.
- ✅ **Fase 5 completada:** Portada personalizada del admin, estilos institucionales, idioma español y diseño adaptable implementados. `manage.py check` pasa; portada revisada en escritorio y móvil.
- 🟡 **Fase 4 implementada, pendiente de prueba integral:** Endpoint y JavaScript AJAX están escritos, pero falta probar el guardado y el tiempo con datos reales.
- ⚠️ **Bloqueo de validación:** Se observó Python 3.14.5 con Django 4.2.16. Una petición a `/admin/asistencia/curso/` falla en `django.template.context.Context.__copy__`; los listados CRUD no están validados.

## Próximas acciones
1. Elegir y probar una combinación compatible de Python y Django que mantenga soporte para MariaDB 10.4.
2. Volver a probar las listas y formularios CRUD del admin.
3. Cargar datos de prueba y validar el flujo AJAX de asistencia, incluido el objetivo de 30 estudiantes en menos de 60 segundos.
4. Actualizar `TASKS.md` y este archivo con los resultados medidos.

## Notas relevantes
- `manage.py check` pasa, pero no reemplaza las pruebas HTTP de las vistas administrativas.
- No declarar cumplido el tiempo objetivo hasta medirlo con datos de prueba.
- La IA no debe ejecutar comandos ni escribir código sin autorización previa (Regla de Oro).