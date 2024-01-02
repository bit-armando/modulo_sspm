from django import forms
from .models import *

class Visita(forms.ModelForm):
    class Meta:
        model = Visitantes
        fields = ['nombres','apellidos','departamento_destino','motivo_visita','folio_gafete','imagen', 'fecha_entrada', 'fecha_salida']
