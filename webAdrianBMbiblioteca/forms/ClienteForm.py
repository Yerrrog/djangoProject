from django import forms
from webAdrianBMbiblioteca.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni','nombre','fechaAlta','direccion','mobile']