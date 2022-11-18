from django.contrib import admin
from .models import Cliente
from .models import Autor
from .models import Libro


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Libro)
admin.site.register(Autor)
