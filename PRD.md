# PRD — Documento de Requisitos del Producto

## Producto
Sistema de Asistencia Express (Uniguajira)

## Problema
Los docentes pierden tiempo valioso de la clase llamando a lista de forma manual. Se requiere un sistema ágil y digital que permita registrar la asistencia de manera inmediata sin flujos complejos.

## Usuarios objetivo
Docentes de la Universidad de La Guajira.

## Objetivo
Desarrollar una aplicación web rápida donde el docente visualice su lista de estudiantes y, con un solo clic por alumno, registre la asistencia en la base de datos.

## Funcionalidades principales (MVP)
1. Inicio de sesión seguro para el docente.
2. Vista en formato lista/tabla de los estudiantes inscritos en el curso.
3. Botón de acción rápida (1 clic) para marcar "Asistió" o "Ausente".
4. Guardado en tiempo real en la base de datos MySQL.
5. Panel administrativo para que el personal autorizado gestione cursos, estudiantes, asistencias y cuentas de acceso.
6. Interfaz administrativa coherente con la identidad visual y utilizable desde pantallas móviles.

## Requisitos Técnicos
- **Lenguaje y Framework:** Python con Django 4.2.16 (LTS).
- **Base de Datos:** MySQL / MariaDB 10.4.32 (XAMPP, puerto 3308, base de datos `asistencia_express`).
- **Frontend:** Bootstrap 5, HTML5, JavaScript.

## Fuera de alcance (Primera versión)
- Aplicación móvil nativa (el sistema será web responsivo).
- Módulo de justificación de excusas médicas.
- Integración con el sistema central de notas.

## Criterios de éxito
- Un docente debe poder tomar la asistencia de un salón de 30 estudiantes en menos de 60 segundos.
- La interfaz requiere máximo un clic por estudiante.
- El personal autorizado puede crear y administrar cursos y estudiantes desde el panel.
- Los cambios de asistencia quedan persistidos y se reflejan sin recargar la página.
- La prueba de los criterios de tiempo y persistencia debe registrarse en `TASKS.md`; mientras no se mida, el criterio permanece pendiente.