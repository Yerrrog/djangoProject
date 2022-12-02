from django.db import models


class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=150, blank=False, null=False)
    autor = models.ForeignKey("Autor", null=False, on_delete=models.CASCADE)
    genero = models.CharField(max_length=150, blank=False, null=True)
    precio = models.FloatField(max_length=150, blank=False, null=True)
