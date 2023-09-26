from django.shortcuts import render
from django.http import HttpResponse
from AppCoderpy.models import Curso, Estudiante, Profesor, Entregable



# Create your views here.
def inicio(request):
    return render(request,"AppCoderpy/inicio.html")

def curso(request):
   return render(request,"AppCoderpy/curso.html")

def estudiante(request):
    return render(request,"AppCoderpy/estudiante.html")

def entregable(request):
    return render(request,"AppCoderpy/entregable.html")

def cursoFormulario(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
        curso.save
        
        return render(request, "AppCoderpy/inicio.html")
    
    return render(request,"AppCoderpy/cursoFormulario.html")