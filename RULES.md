# RULES — ¿Qué debe y no debe hacer la IA al programar?

## Regla de oro
**No ejecutar nada (instalar librerías, crear carpetas, correr scripts, o modificar base de datos) sin que el usuario lo indique explícitamente.** El usuario ha pedido dejar todo documentado primero y él irá señalando qué ejecutar, en qué momento y en qué archivo.

## Debe hacer
- Trabajar siempre dentro del entorno virtual `venv/` para cualquier dependencia de Python.
- Respetar estrictamente la separación de carpetas: lógica de Python va en `backend/` y las vistas/diseño van en `frontend/`.
- Usar el ORM de Django de forma idiomática (evitar iterar con bucles `for` si se puede usar una consulta directa a la base de datos como `.update()` o `.filter()`).
- Nombrar variables, funciones y archivos en `snake_case`, en español de forma consistente.
- Seguir PEP8 para el formato del código Python.
- Documentar en [DECISIONS.md](DECISIONS.md) cualquier elección técnica relevante y por qué se tomó.
- Actualizar [TASKS.md](TASKS.md) y [MEMORY.md](MEMORY.md) conforme avance el proyecto.
- Antes de borrar o sobreescribir un archivo con código existente, confirmar primero con el usuario.

## No debe hacer
- No instalar paquetes, crear proyectos de Django ni correr migraciones de forma proactiva; esperar indicación explícita del usuario.
- No sobre-diseñar: no crear abstracciones o configuraciones avanzadas que el alcance del ejercicio no requiere.
- No agregar manejo de errores excesivo para casos que no pueden ocurrir en este contexto académico.
- No romper la regla visual: No usar colores que se salgan de la paleta institucional (Verde, Blanco, Negro) definida en [DESIGN.md](DESIGN.md) ni mezclar tipos de letras.
- No dejar código o plantillas HTML a medio terminar; cada script o vista debe entregarse completo.
- No commitear ni incluir contraseñas reales o claves secretas en los archivos del repositorio (usar siempre variables de entorno).

## Seguimiento y validación
- Registrar en `TASKS.md` cada funcionalidad implementada y cada prueba pendiente; no marcar una prueba como hecha solo porque el código existe.
- Mantener `MEMORY.md` y `REPORTE.md` coherentes con los resultados realmente observados.
- Documentar las versiones de Python, Django y base de datos usadas, y probar su compatibilidad antes de dar por válido el admin o el MVP.
- Distinguir entre `manage.py check` y las pruebas de comportamiento: ambas aportan información distinta.