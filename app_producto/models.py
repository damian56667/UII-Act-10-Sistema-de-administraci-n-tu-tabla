from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio_venta = models.FloatField()
    stock = models.PositiveIntegerField()
    id_marca = models.PositiveIntegerField()
    id_famillia = models.PositiveIntegerField()  # usé la doble 'll' como pediste

    def __str__(self):
        return f'Producto: {self.nombre}'
