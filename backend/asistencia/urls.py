from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.lista_estudiantes, name='lista_estudiantes'),
    path('curso/<int:curso_id>/', views.lista_estudiantes, name='curso_asistencia'),
    path('asistencia/marcar/', views.marcar_asistencia, name='marcar_asistencia'),
]
