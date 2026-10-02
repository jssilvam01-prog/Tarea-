from django.contrib import admin
from .models import Curso, Estudiante, Asistencia


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "docente")
    search_fields = ("codigo", "nombre", "docente__username")
    list_filter = ("docente",)


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("codigo", "apellido", "nombre", "curso")
    search_fields = ("codigo", "apellido", "nombre")
    list_filter = ("curso",)


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "estudiante", "curso", "estado")
    list_filter = ("fecha", "curso", "estado")
    search_fields = ("estudiante__nombre", "estudiante__apellido", "estudiante__codigo")
