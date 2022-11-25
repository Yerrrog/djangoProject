from django.urls import path
from . import views

urlpatterns = [
                path('',views.clientes_list,name='clientes_list'),
                path('nuevoCliente/ ', views.cliente_new,name='cliente_new'),
                path('borrarCliente/<int:id_alumno>',views.cliente_delete())
               ]