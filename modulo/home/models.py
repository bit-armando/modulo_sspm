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
    
    class Meta:
        ordering = ['-fecha_entrada']

    def __str__(self):
        return self.nombres + ' ' + self.apellidos


# class Conteo(models.Model):
#     fecha = models.DateField(auto_now_add=True)
#     llamadas_recibidas = models.IntegerField()
#     informacion_detenidos = models.IntegerField()
#     informacion_tramites = models.IntegerField()
#     visitas_detenidos = models.IntegerField()
#     quejas = models.IntegerField()

#     def __str__(self):
#         return str(self.fecha)
    