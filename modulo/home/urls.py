from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salida/', views.salida, name='salida'),
    path('marcar_salida/<int:visitante_id>/', views.marcar_salida, name='marcar_salida'),
    path('registro_entrada/', views.registrar_entrada, name='registrar_entrada')
]