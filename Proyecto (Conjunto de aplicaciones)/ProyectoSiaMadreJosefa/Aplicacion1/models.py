from django.db import models


# Create your models here.

class Personas(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=True)
    nacionalidad = models.CharField(max_length=20, null=False, blank=True)
    correoElectronico = models.EmailField(null=True, blank=True)
    numeroContacto = models.IntegerField( blank=False, null=False)
    direccion = models.TextField(max_length=100, blank=False, null=False)
    ciudad = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        abstract = True


class Operadores(Personas):
    rut = models.IntegerField( null=False, blank=False, primary_key= True)
    cargo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nombre, self.rut


class Patendidas(Personas):
    #idPatendida = models.AutoField()
    rut_DNI = models.CharField(max_length=20, null=True, blank=True)
    estadosCiviles = [('1', "Soltero"), ('2', "Sasado")]
    estadoCivil = models.CharField(max_length= 7, null=False, blank=False, choices=estadosCiviles)
    hijosChoice = [('1', "Si"), ('2', "No")]
    hijos = models.CharField(max_length=2, null=False, blank=False, choices=hijosChoice)
    cantHijos = models.IntegerField( null=False, blank=False)
    fechaIngreso = models.DateField( null=False, blank=False)
    motivoIngreso = models.CharField(max_length=300, null=False, blank=False)


class Ficha(models.Model):
    #idFicha = models.AutoField()
    encargado = models.CharField(max_length=50, null=False, blank=False)
    nombrePatendida = models.CharField(max_length=50, null=False, blank=False)
    fecha = models.DateField( null=False, blank=False)
    detalle = models.TextField(max_length=600, null=False, blank=False)
    tiposUrgencias = [('1', "Leve"), ('2', "Media"), ('2', "Grave")]
    urgenciaCaso = models.CharField(max_length=5, null=False, blank=False, choices=tiposUrgencias)
    tipoApoyo = models.CharField(max_length=30, null=False, blank=False)
