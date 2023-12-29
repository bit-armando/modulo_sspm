from django.shortcuts import render, redirect
from django.utils import timezone

import cv2

from .models import Visitantes

# Vista de la ingesta de los datos
def index(request):
    context = {}
    return render(request, 'home/index.html', context)

def registrar_entrada(request):
    if request.method == 'POST':
        nombre = request.POST['nombres']
        apellido = request.POST['apellido_paterno'] + ' ' + request.POST['apellido_materno']
        departamento = request.POST['departamento']
        motivo = request.POST['motivo']
        folio = request.POST['folio_gafete']
        visitante = Visitantes(nombres=nombre, apellidos=apellido, departamento_destino=departamento, motivo_visita=motivo, folio_gafete=folio)
        visitante.save()
        
        
        return render(request, 'home/index.html', {})
    context = {}
    return render(request, 'home/index.html', context)

def salida(request):
    visitantes_activos = Visitantes.objects.filter(fecha_salida__isnull=True)
    context = {
        'visitantes_activos': visitantes_activos,
    }
    return render(request, 'home/salida.html', context)
def marcar_salida(request, visitante_id):
    visitante = Visitantes.objects.get(pk=visitante_id)
    visitante.fecha_salida = timezone.now()
    visitante.save()
    return redirect('salida')
