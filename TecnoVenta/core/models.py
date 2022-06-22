from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria =models.IntegerField(default=1, primary_key=True, verbose_name='Id Categoria')
    nombreCategoria =models.CharField(max_length=30, verbose_name='Categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id Producto')
    marca = models.CharField(max_length=30, verbose_name='Marca Producto')
    precio = models.CharField(max_length=20, verbose_name='Precio')
    modelo = models.CharField(max_length=30, verbose_name='Modelo Producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):

        return self.marca
        
        
