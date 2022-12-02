from django.db import models


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    descripcion = models.CharField(max_length=50,blank=False,null=False)