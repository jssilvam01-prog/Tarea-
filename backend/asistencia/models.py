from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Curso(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Curso")
    codigo = models.CharField(max_length=30, unique=True, verbose_name="Código")
    docente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cursos", verbose_name="Docente")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    codigo = models.CharField(max_length=30, unique=True, verbose_name="Código Estudiantil")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="estudiantes", verbose_name="Curso")

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - {self.codigo}"


class Asistencia(models.Model):
    ESTADO_CHOICES = [
        ("ASISTIO", "Asistió"),
        ("AUSENTE", "Ausente"),
    ]

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="asistencias", verbose_name="Estudiante")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="asistencias", verbose_name="Curso")
    fecha = models.DateField(default=timezone.localdate, verbose_name="Fecha")
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default="AUSENTE", verbose_name="Estado")

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        unique_together = ("estudiante", "curso", "fecha")
        ordering = ["-fecha", "estudiante"]

    def __str__(self):
        return f"{self.fecha} | {self.estudiante.nombre} {self.estudiante.apellido} -> {self.get_estado_display()}"
