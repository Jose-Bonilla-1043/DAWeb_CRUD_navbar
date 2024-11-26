from django.db import models

class Venta(models.Model):
    id_venta = models.CharField(primary_key=True, max_length=6)  # ID único para la venta
    fecha = models.DateField()  # Cambiado a DateField para almacenar fechas correctamente
    estado = models.CharField(max_length=50)  # Por ejemplo pendiente, completada ...
    cantidad = models.PositiveIntegerField()  # Número de unidades vendidas
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)  # Para almacenar precios con decimales
    id_producto = models.TextField(blank=True, null=True)  # Relación con el producto, pendiente de mejora
    id_empleado = models.CharField(max_length=10, blank=True, null=True)  # Añadido correctamente
    id_cliente = models.CharField(max_length=10, blank=True, null=True)  # Añadido correctamente


    def __str__(self):
        return self.id_venta
