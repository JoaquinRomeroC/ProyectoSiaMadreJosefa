from django.http import HttpResponse
from django.shortcuts import render

from Aplicacion1.models import Operadores


def ejemplo(request):
    return HttpResponse("Hola Mundo")

def ejemplo2(request):
    return  render(request,'Home.html')

def inicioSesion(request):
    return render(request, 'Inicio Sesion.html')

def listadoOperadores(request):
    operadores: {'listadoOperadores': Operadores.objects.all ()}
    return render(request, 'Operadores.html', datos)






