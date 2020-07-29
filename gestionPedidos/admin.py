from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos  # importando las clases de models

# Register your models here.

"""
Aqui es donde se codificara todo lo necesario para poder gestionar las tablas en la BBDD

OJO: Puede que para algunas modificaciones haya que reiniciar el servidor para poder aplicar los cambios.

"""

admin.site.register(Clientes)
admin.site.register(Articulos)
admin.site.register(Pedidos)


