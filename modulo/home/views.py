# from django.shortcuts import render
from django.http import HttpResponse

# Vista de la ingesta de los datos
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")