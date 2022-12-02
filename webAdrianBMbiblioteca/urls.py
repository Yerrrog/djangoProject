from django.urls import path
from . import views

urlpatterns = [
                path('',views.listaCliente,name='listaCliente'),
                path('nuevoCliente/ ', views.nuevoCliente,name='nuevoCliente'),
                path('nuevoLibro/',views.nuevoLibro,name='nuevoLibro')
               ]