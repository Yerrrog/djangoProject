from django.db import models


class Cliente(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    fechaAlta = models.DateField('Fecha Alta', blank=False, null=False)
    direccion = models.CharField(max_length=150, blank=False, null=True)
    mobile = models.CharField(max_length=150, blank=False, null=True)


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=False)


class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=150, blank=False, null=False)
    autor = models.ForeignKey("Autor", null=False, on_delete=models.CASCADE)
    genero = models.CharField(max_length=150, blank=False, null=True)
    precio = models.FloatField(max_length=150, blank=False, null=True)
