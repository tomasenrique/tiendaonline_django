from django.db import models


# Create your models here.

#  Aqui se estan creando las clases que luego pasaran a ser las tablas
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=10)


"""
 Al agregar 'blank=True, null=True' se hace que el campo sea opcional a la hora de crear un cliente en la web
"""


class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    # Esto sera para poder ver el contenido a la hora de hacer consultas a la BBDD
    def __str__(self):
        return "El nombre es: %s - La sección es: %s - El precio es: %s" % (self.nombre, self.seccion, self.precio)

    """OJO
        Cada vez que se haga modificaciones aqui, hay que volver a hacer las migraciones a la BBDD para que se agrege 
        este cambio y se pueda ver las consultas hechas en este caso.
        
        PRIMERO CON: python manage.py makemigrations
        
        SEGUNDO CON: python manage.py migrate
        
        y listo    """


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
