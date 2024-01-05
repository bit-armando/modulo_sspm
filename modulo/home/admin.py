from django.contrib import admin

from .models import Visitantes

class VisitantesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'departamento_destino', 'motivo_visita', 'folio_gafete')
    # fields = ['nombres', 'apellidos', 'departamento_destino', 'motivo_visita', 'folio_gafete', 'imagen', 'fecha_salida']

admin.site.register(Visitantes, VisitantesAdmin)
# admin.site.register(Conteo)
