from django.http import HttpResponse
from django.template import Template, Context
import datetime as dt 

def saludo(request):
    return HttpResponse("hola mundo")

def fecha(request):
    ahora = dt.datetime.now()
    return HttpResponse(ahora)

def index (recuest):
    Index_Html = open("C:/Python/Clase18/Proyecto/Proyecto/plantillas/index.html")
    plantilla = Template(Index_Html.read())
    Index_Html.close()
    
    contex1 = Context()
    return HttpResponse(plantilla.render(contex1))