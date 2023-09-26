from django.shortcuts import render
from django.http import HttpResponse
from AppCoderpy.models import Curso
from AppCoderpy.forms import CursoFormulario



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
        
        formulario1 = CursoFormulario(request.POST)
        
        if formulario1.is_valid():

            info = formulario1.cleaned_data
            curso = Curso(nombre=info["nombre"], camada=info["camada"])
            curso.save
        
            return render(request, "AppCoderpy/inicio.html")
        else:
            formulario1 = CursoFormulario()    
    return render(request,"AppCoderpy/cursoFormulario.html",{"form1":formulario1})


