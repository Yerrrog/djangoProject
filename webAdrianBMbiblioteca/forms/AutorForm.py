from django import forms
from webAdrianBMbiblioteca.models import Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['id', 'nombre','descripcion']
2