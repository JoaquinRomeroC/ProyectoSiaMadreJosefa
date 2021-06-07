from django.urls import path
from Aplicacion1.views import *

urlpatterns = [

    path('', Home, name = 'home'),
    path('login/', Login),
    path('operadores/', listadoOperadores, name = 'lOperadores')






]