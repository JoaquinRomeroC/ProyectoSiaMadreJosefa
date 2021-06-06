from django.db import models


# Create your models here.

class Personas(models.Model):
    nombre: models.CharField(max_length=100, null=False, blank=True)
    nacionalidad: models.CharField(max_length=20, null=False, blank=True)
    correoElectronico: models.EmailField(null=True, blank=True)
    numeroContacto: models.IntegerField(max_length=10, blank=False, null=False)
    direccion: models.CharField(max_length=100, blank=False, null=False)
    ciudad: models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        abstract = True


class Operadores(Personas):
    rut: models.IntegerField(max_length=9, null=False, blank=False, primary_key=True)
    cargo: models.CharField(max_length=100, null=False, blank=False)


class Patendidas(Personas):
    idPatendida: models.CharField(primary_key=True)
    rut_DNI: models.CharField(max_length=20, null=True, blank=True)
    estadosCiviles = [('1', "Soltero"), ('2', "Sasado")]
    estadoCivil: models.CharField(null=False, blank=False, choices=estadosCiviles)
    hijosChoice = [('1', "Si"), ('2', "No")]
    hijos: models.CharField(max_length=2, null=False, blank=False, choices=hijosChoice)
    cantHijos: models.IntegerField(max_length=2, null=False, blank=False)
    fechaIngreso: models.DateField(max_length=15, null=False, blank=False)
    motivoIngreso: models.CharField(max_length=300, null=False, blank=False)


class Ficha(models.Model):
    idFicha: models.CharField(primary_key=True)
    encargado: models.CharField(max_length=50, null=False, blank=False)
    nombrePatendida: models.CharField(max_length=50, null=False, blank=False)
    fecha: models.DateField(max_length=15, null=False, blank=False)
    detalle: models.CharField(max_length=600, null=False, blank=False)
    tiposUrgencias = [('1', "Leve"), ('2', "Media"), ('2', "Grave")]
    urgenciaCaso: models.CharField(null=False, blank=False, choices=tiposUrgencias)
    tipoApoyo: models.CharField(max_length=30, null=False, blank=False)
