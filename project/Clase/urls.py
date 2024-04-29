
from django.urls import path
from . import views

app_name = "Clase"

urlpatterns = [
    path('',views.home, name="home"),
    path('Cursos/agregarCurso/',views.agregarCurso, name="agregarCurso"),
    path('Cursos/agregarProfesor/',views.agregarProfesor, name="agregarProfesor"),
    path('Cursos/agregarEstudiante/',views.agregarEstudiante, name="agregarEstudiante"),
]