from django.contrib import admin

from .models import Visitantes

class VisitantesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'departamento_destino', 'motivo_visita', 'folio_gafete')
    list_editable = ('departamento_destino', 'motivo_visita', 'folio_gafete')

admin.site.register(Visitantes, VisitantesAdmin)
# admin.site.register(Conteo)
