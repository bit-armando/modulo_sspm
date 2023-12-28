# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import cv2

from .models import Visitantes

# Vista de la ingesta de los datos
def index(request):
    template = loader.get_template('home/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def capturar_imagen(request):
    template = loader.get_template('home/capturar_imagen.html')
    context = {}
    return HttpResponse(template.render(context, request))

def salida(request):
    visitantes_activos = Visitantes.objects.filter(fecha_salida__isnull=True)
    template = loader.get_template('home/salida.html')
    context = {
        'visitantes_activos': visitantes_activos,
    }
    return HttpResponse(template.render(context, request))
