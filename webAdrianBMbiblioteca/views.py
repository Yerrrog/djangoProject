from django.shortcuts import render
from .models import Cliente
from django.utils import timezone
from .forms import ClienteForm
from django.views.generic import CreateView

# Create your views here.
def clientes_list(request):
    clientes = Cliente.objects.filter(fechaAlta__lte=timezone.now()).order_by('fechaAlta')
    return render(request, 'clientes_list.html', {'clientes':clientes})

def cliente_new(request):
    if request.method =='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
    else:
        form = ClienteForm()
    return render(request,'cliente_edit.html',{'form':form})