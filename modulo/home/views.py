# from django.shortcuts import render
from django.http import HttpResponse

# Vista de la ingesta de los datos
def index(request):
    return HttpResponse("Holi Marco UwU.")