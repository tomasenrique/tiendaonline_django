from gestionPedidos.models import Articulos

# Para insertar en la tabla
art1 = Articulos.objects.create(nombre='lampara', seccion='decoración', precio=65)
art2 = Articulos.objects.create(nombre='pantalon', seccion='confección', precio=65)
art3 = Articulos.objects.create(nombre='destornillador', seccion='ferreteria', precio=65)
art4 = Articulos.objects.create(nombre='balon', seccion='deportes', precio=65)
art5 = Articulos.objects.create(nombre='raqueta', seccion='deportes', precio=65)
art6 = Articulos.objects.create(nombre='muñeca', seccion='jugueteria', precio=65)
art7 = Articulos.objects.create(nombre='tren eléctrico', seccion='jugueteria', precio=65)
art8 = Articulos.objects.create(nombre='mesa', seccion='jugueteria', precio=120)

# ======================================================================================================================
# CONSULTAS A LA BBDD

# ==>> UN CRITERIO
# Estos es para buscar areas, similar a usar where en sql, esta es una consulta con 1 solo criterio
Articulos.objects.filter(seccion='deportes')

Articulos.objects.filter(seccion='decoracion')

# ==>> DOS CRITERIOS
# 'precio__gte' es igual a mayor que '>'
Articulos.objects.filter(seccion='deportes', precio__gte=100)  # OJO el 'precio__gte' es solo para la consola de python

# 'precio__lte' es igual a menor que '<'
Articulos.objects.filter(seccion='deportes', precio__lte=100)  # OJO el 'precio__gte' es solo para la consola de python

Articulos.objects.filter(nombre='mesa', seccion='decoracion')  # articulo de decoracion
Articulos.objects.filter(nombre='mesa', seccion='jugueteria')  # articulo de jugueteria

# ==>> CONSULTA CON UNA FUNCION ==>> __range=[min, max] para ubicar valores entre rangos
Articulos.objects.filter(seccion='jugueteria', precio__range=[30, 130])  # articulo de jugueteria

# ==>> CONSULTA Y ORDENADO - ORDER BY de menor a mayor
Articulos.objects.filter(precio__gte=50).order_by('precio')

# ==>> CONSULTA Y ORDENADO - ORDER BY de mayor a menor
Articulos.objects.filter(precio__gte=50).order_by('-precio')
# ======================================================================================================================
