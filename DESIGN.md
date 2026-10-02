# DESIGN — Sistema de Diseño

## Estilo General
Institucional, limpio, rápido y enfocado en la usabilidad extrema.

## Identidad Visual (Uniguajira)
- **Logotipo:** Escudo oficial de la Universidad de La Guajira visible en la barra de navegación (Navbar).
- **Paleta de Colores Estricta:**
  - **Primario (Énfasis/Éxito):** Verde institucional Uniguajira.
  - **Fondo principal:** Gris muy claro (`#F8F9FA`) con superficies de contenido blancas (`#FFFFFF`) para máxima legibilidad.
  - **Texto:** Negro (`#000000`) y grises oscuros.
  - **Secundario (Ausencia/Peligro):** Gris oscuro (evitar colores estridentes que no sean de la marca).

## Tipografía y UI
- **Un solo formato de letras:** Se utilizará una única familia tipográfica para absolutamente toda la plataforma (ej. Roboto, provista por Bootstrap). No se deben mezclar diferentes tipos de letras (fuentes) entre títulos, botones y textos para mantener una estética uniforme y seria.
- **Diseño de Lista:** Tabla con filas amplias o tarjetas (cards) limpias.
- **Interacción:** El botón de asistencia debe ser grande, fácil de tocar en pantallas móviles, y cambiar de estado visual inmediatamente al hacer clic.

## Panel de Administración
- Mantener el encabezado institucional verde con el escudo, la marca Uniguajira y el nombre del sistema.
- Usar fondo gris claro y secciones blancas con bordes discretos; reservar el verde para encabezados y acciones principales.
- Organizar Cursos, Estudiantes, Asistencias y permisos en secciones fáciles de recorrer, con acciones visibles para agregar y administrar.
- Mantener Roboto, idioma español, adaptación a móvil y tema claro, sin depender de la preferencia oscura del sistema operativo.
- Las páginas CRUD deben conservar las funciones nativas de Django; el estilo no se considera validado hasta probar también esas páginas.