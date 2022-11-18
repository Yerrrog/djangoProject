from django import forms
from .models import Cliente
from .models import Autor
from .models import Libro

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni','nombre','fechaAlta','direccion','mobile']
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['id','nombre']


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['isbn', 'titulo', 'autor', 'genero', 'precio']
