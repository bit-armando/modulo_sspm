# Modelo de los visitantes
from django.db import models

class Visitantes(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    departamento_destino = models.CharField(max_length=50)
    motivo_visita = models.CharField(max_length=100)
    folio_gafete = models.IntegerField()
    imagen = models.ImageField(upload_to='images/', blank=False, null=True)
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)  

    def __str__(self):
        return self.nombres + ' ' + self.apellidos
    