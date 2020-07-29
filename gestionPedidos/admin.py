from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos  # importando las clases de models

# Register your models here.

"""
Aqui es donde se codificara todo lo necesario para poder gestionar las tablas en la BBDD

OJO: Puede que para algunas modificaciones haya que reiniciar el servidor para poder aplicar los cambios.
"""

""" 
Con esta clase 'clientesAdmin' se configura que campos mostrar en la vista como si fuera una tabla, se aplicara luego 
en la linea correspondiente """


class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono")  # Para mostrar los campos que querramos en la vista
    search_fields = ("nombre", "telefono")  # Para agregar una barra de busqueda con los campos especificados


class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ("seccion",)  # Para agregar en el laterial derecho una caja para filtrar por el campo especificado


# el 'list_filter' usa una tupla por eso la coma del final

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha")  # Para mostrar los campos que querramos en la vista
    list_filter = ("fecha",)  # Para agregar en el laterial derecho una caja para filtrar por el campo especificado
    date_hierarchy = "fecha"  # Para filtrar por fecha los pedidos.


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
