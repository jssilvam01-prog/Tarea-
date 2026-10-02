import json
from django.contrib.auth.models import User
from django.http import Http404
from django.test import RequestFactory, TestCase
from django.urls import reverse
from .models import Asistencia, Curso, Estudiante
from .views import lista_estudiantes, marcar_asistencia


class AccesoAsistenciaTests(TestCase):
	def setUp(self):
		self.request_factory = RequestFactory()
		self.docente = User.objects.create_user(username='docente', password='clave-segura')
		self.otro_docente = User.objects.create_user(username='otro', password='clave-segura')
		self.curso = Curso.objects.create(nombre='Matemáticas', codigo='MAT101', docente=self.docente)
		self.otro_curso = Curso.objects.create(nombre='Física', codigo='FIS101', docente=self.otro_docente)
		self.estudiante = Estudiante.objects.create(
			nombre='Ana', apellido='Pérez', codigo='EST001', curso=self.curso
		)

	def test_lista_requiere_inicio_de_sesion(self):
		response = self.client.get(reverse('lista_estudiantes'))

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['Location'], f'{reverse("login")}?next={reverse("lista_estudiantes")}')

	def test_docente_no_puede_abrir_curso_ajeno(self):
		request = self.request_factory.get('/')
		request.user = self.docente

		with self.assertRaises(Http404):
			lista_estudiantes(request, self.otro_curso.id)

	def test_marcar_asistencia_guarda_estado_del_estudiante_del_docente(self):
		self.client.force_login(self.docente)

		response = self.client.post(
			reverse('marcar_asistencia'),
			data=json.dumps({'estudiante_id': self.estudiante.id, 'curso_id': self.curso.id}),
			content_type='application/json',
		)

		self.assertEqual(response.status_code, 200)
		self.assertTrue(response.json()['asistio'])
		self.assertEqual(Asistencia.objects.get(estudiante=self.estudiante).estado, 'ASISTIO')

	def test_no_se_puede_marcar_estudiante_de_otro_curso(self):
		request = self.request_factory.post(
			reverse('marcar_asistencia'),
			data=json.dumps({'estudiante_id': self.estudiante.id, 'curso_id': self.curso.id}),
			content_type='application/json',
		)
		request.user = self.otro_docente

		with self.assertRaises(Http404):
			marcar_asistencia(request)
		self.assertFalse(Asistencia.objects.exists())
