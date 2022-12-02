from django.shortcuts import render
from .models import Cliente
from django.utils import timezone
from .forms import ClienteForm
from .forms import LibroForm
from django.views.generic import CreateView


# Create your views here.
def listaCliente(request):
    clientes = Cliente.objects.filter(fechaAlta__lte=timezone.now()).order_by('fechaAlta')
    return render(request, 'clientes_list.html', {'clientes': clientes})


def nuevoCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
    else:
        form = ClienteForm()
    return render(request, 'cliente_create.html', {'form': form})


def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    cliente.delete()
    clientes = Cliente.objects.all()
    return render(request, "clientes_list.html", {"clientes": clientes})


def nuevoLibro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.save()
    else:
        form = LibroForm()
    return render(request, 'libro_create.html', {'form': form})
