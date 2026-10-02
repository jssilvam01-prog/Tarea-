import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Curso, Estudiante, Asistencia


@login_required
def lista_estudiantes(request, curso_id=None):
    """
    Vista principal que muestra la lista de estudiantes inscritos
    en un curso y su estado de asistencia para el día de hoy.
    """
    if request.user.is_superuser:
        cursos = Curso.objects.all()
    else:
        cursos = Curso.objects.filter(docente=request.user)

    fecha_hoy = timezone.localdate()

    if curso_id:
        curso = get_object_or_404(cursos, id=curso_id)
    else:
        curso = cursos.first()

    estudiantes_data = []
    total_presentes = 0
    total_ausentes = 0

    if curso:
        estudiantes = curso.estudiantes.all()
        # Consultar asistencias registradas hoy para este curso
        asistencias_hoy = Asistencia.objects.filter(curso=curso, fecha=fecha_hoy).values('estudiante_id', 'estado')
        asistencias_map = {a['estudiante_id']: a['estado'] for a in asistencias_hoy}

        for est in estudiantes:
            estado = asistencias_map.get(est.id, 'AUSENTE')
            asistio = (estado == 'ASISTIO')
            if asistio:
                total_presentes += 1
            estudiantes_data.append({
                'estudiante': est,
                'asistio': asistio,
                'estado': estado,
            })
        total_ausentes = len(estudiantes_data) - total_presentes

    context = {
        'curso': curso,
        'cursos': cursos,
        'total_cursos': cursos.count(),
        'fecha': fecha_hoy,
        'estudiantes_data': estudiantes_data,
        'total_estudiantes': len(estudiantes_data),
        'total_presentes': total_presentes,
        'total_ausentes': total_ausentes,
    }
    return render(request, 'estudiantes_lista.html', context)


@login_required
@require_POST
def marcar_asistencia(request):
    """
    Endpoint AJAX de alta velocidad: registra o alterna la asistencia
    de un estudiante en un solo clic, guardando en tiempo real en MySQL.
    """
    try:
        data = json.loads(request.body)
        estudiante_id = data.get('estudiante_id')
        curso_id = data.get('curso_id')
    except (ValueError, KeyError, TypeError):
        return JsonResponse({'status': 'error', 'mensaje': 'Petición con formato inválido'}, status=400)

    if request.user.is_superuser:
        curso = get_object_or_404(Curso, id=curso_id)
    else:
        curso = get_object_or_404(Curso, id=curso_id, docente=request.user)
    estudiante = get_object_or_404(Estudiante, id=estudiante_id, curso=curso)
    fecha_hoy = timezone.localdate()

    # Buscar o crear la asistencia del día usando el ORM idiomático
    asistencia, creada = Asistencia.objects.get_or_create(
        estudiante=estudiante,
        curso=curso,
        fecha=fecha_hoy,
        defaults={'estado': 'ASISTIO'}
    )

    if not creada:
        # Alternar de forma inmediata: si asistió pasa a ausente, y viceversa
        asistencia.estado = 'AUSENTE' if asistencia.estado == 'ASISTIO' else 'ASISTIO'
        asistencia.save(update_fields=['estado'])

    asistio = (asistencia.estado == 'ASISTIO')

    return JsonResponse({
        'status': 'ok',
        'estudiante_id': estudiante.id,
        'asistio': asistio,
        'estado': asistencia.estado,
        'mensaje': 'Asistencia actualizada correctamente'
    })
