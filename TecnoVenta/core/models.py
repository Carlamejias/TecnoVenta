from django.db import models

# Create your models here.

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id Producto')
    marca = models.CharField(max_length=30, verbose_name='Marca Producto')
    precio = models.IntegerField(verbose_name='Precio')
    modelo = models.CharField(max_length=30, verbose_name='Modelo Producto')
    categoria = models.CharField(max_length=30, verbose_name='Categoria')

    def __str__(self):

        return self.marca
        
        
