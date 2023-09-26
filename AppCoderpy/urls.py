from django.urls import path
from AppCoderpy.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("curso/", curso, name="Cursos"),
    path("estudiante/", estudiante, name="Estudiantes"),
    path("entregable/", entregable, name="Entregable"),
    path("cursoFormulario/", cursoFormulario, name="CursoFormulario"),
]
