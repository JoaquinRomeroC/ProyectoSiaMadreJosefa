from django.http import HttpResponse
from django.shortcuts import render

from Aplicacion1.models import *
from django.views.generic import ListView

def ejemplo(request):
    return HttpResponse("Hola Mundo")

def ejemplo2(request):
    return  render(request,'.html')

def Home(request):
    return render(request, 'Home.html')

def Login(request):
    return render(request, 'Login.html')

def listadoOperadores(request):
    operadores = {'listaPersonas': Operadores.objects.all}
    return render(request, 'ListaOperadores.html', datosOperadores)







