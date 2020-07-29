from gestionPedidos.models import Articulos

# Aqui se va a realizar pruebas para hacer CRUD a la BBDD de SqlLite

# INSERT
art1 = Articulos(nombre='mesa', seccion='decoracion', precio=90)
art1.save()  # Con esto se ingresan los datos a la BBDD

art2 = Articulos(nombre='camisa', seccion='confeccion', precio=75)
art2.save()

# Aqui es otra forma de insertar datos
art3 = Articulos.objects.create(nombre='taladro', seccion='ferreteria', precio=65)

# ======================================================================================================================
# UPDATE

art1.precio = 105
art1.save()

# ======================================================================================================================
# DELETE

art4 = Articulos.objects.get(id=2)
art4.delete()
#  mostrara lo siguiente, indicando que se ha borrado ==>> (1, {'gestionPedidos.Articulos': 1})

# ======================================================================================================================
# READ
lista = Articulos.objects.all()  # Obtiene todos los registros de la BBDD

#  Ahora escribir ==>> lista y enter y mostrara lo siguiente:
#  <QuerySet [<Articulos: Articulos object (1)>, <Articulos: Articulos object (3)>]>

lista.query.__str__()  # Mostrara la query para mostrar los datos

'SELECT "gestionPedidos_articulos"."id", "gestionPedidos_articulos"."nombre", "gestionPedidos_articulos"."seccion", "gestionPedidos_articulos"."precio" FROM "gestionPedidos_articulos"'

# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


# Aqui se va a realizar pruebas para hacer CRUD a la BBDD de Postgree

from gestionPedidos.models import Clientes

cli1 = Clientes(nombre='Tomas', direccion='mi casa', telefono='640622')
cli1.save()


cli2 = Clientes.objects.create(nombre='Jonas', direccion='iberia', email='tomasenriquea@hotmail.com', telefono='123456')


# ======================================================================================================================
#  Hay que probarlo desde la consola ingresando usando:
# python manage.py shell
