from django.forms import forms
from webAdrianBMbiblioteca.models import Prestamo



class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['cliente', 'libro', 'fechaPrestamo']