from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos  # importando las clases de models

# Register your models here.

"""
Aqui es donde se codificara todo lo necesario para poder gestionar las tablas en la BBDD

OJO: Puede que para algunas modificaciones haya que reiniciar el servidor para poder aplicar los cambios.
"""

""" 
Con esta clase se configura que campos mostrar en la vista como si fuera una tabla, se aplicara luego en la linea 
correspondiente """


class clientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono")  # Para mostrar los campos que querramos en la vista
    search_fields = ("nombre", "telefono")  # Para agregar una barra de busqueda con los campos especificados


admin.site.register(Clientes, clientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)
