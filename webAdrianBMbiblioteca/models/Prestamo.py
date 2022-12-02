from django.db import models


class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    libro = models.ForeignKey("Libro", on_delete=models.CASCADE)
    fechaPrestamo = models.DateField('Fecha de Prestamo', blank=False, null=False)
    '''fechaDevolucion = fechaPrestamo + 15'''

