from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView

from .models import Visitantes

# Vista de la ingesta de los datos
def index(request):
    context = {}
    return render(request, 'index.html', context)

def registrar_entrada(request):
    if request.method == 'POST':

        nombre = request.POST['nombres']
        apellido = request.POST['apellido_paterno'] + ' ' + request.POST['apellido_materno']
        departamento = request.POST['departamento']
        motivo = request.POST['motivo']
        folio = request.POST['folio_gafete']
        
        image = request.FILES['imagen']
        image.name = str(timezone.now().year) + '_' + str(timezone.now().month) + '_' + str(timezone.now().day) + '_' + str(nombre) + str(folio) + '.jpg'
        
        visitante = Visitantes(nombres=nombre, apellidos=apellido, departamento_destino=departamento, motivo_visita=motivo, folio_gafete=folio, imagen=image)
        visitante.save()

        return render(request, 'index.html', {})
    return render(request, 'index.html', {})

def salida(request):
    visitantes_activos = Visitantes.objects.filter(fecha_salida__isnull=True)
    context = {
        'visitantes_activos': visitantes_activos,
    }
    return render(request, 'salida.html', context)
def marcar_salida(request, visitante_id):
    visitante = Visitantes.objects.get(pk=visitante_id)
    visitante.fecha_salida = timezone.now()
    visitante.save()
    return redirect('salida')


class Consulta(ListView):
    model = Visitantes
    template_name = 'consulta.html'
    context_object_name = 'visitantes'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        fecha_inicio = self.request.GET.get('fecha_inicio', None)
        
        if fecha_inicio:
            queryset = queryset.filter(
                fecha_entrada__date=fecha_inicio
            )

        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fecha_inicio = self.request.GET.get('fecha_inicio', None)
        
        if fecha_inicio:
            context['fecha_inicio'] = fecha_inicio

        return context
