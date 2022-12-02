from django import forms
from webAdrianBMbiblioteca.models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['isbn', 'titulo', 'autor', 'genero', 'precio']
