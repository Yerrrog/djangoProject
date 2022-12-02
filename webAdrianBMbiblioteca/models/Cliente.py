from django.db import models


class Cliente(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    fechaAlta = models.DateField('Fecha Alta', blank=False, null=False)
    direccion = models.CharField(max_length=150, blank=False, null=True)
    mobile = models.CharField(max_length=150, blank=False, null=True)
    'faltas = models.IntegerField()'

