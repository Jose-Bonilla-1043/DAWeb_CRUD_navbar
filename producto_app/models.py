from django.db import models

class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=6)  # Clave primaria con un máximo de 6 caracteres
    nombre = models.CharField(max_length=100)  # Nombre del producto como texto
    descripcion = models.TextField()  # Descripción como texto largo
    tamano = models.CharField(max_length=50)  # Tamaño como texto (ej. '20 cm', '500 ml')
    color = models.CharField(max_length=100)  # Color como texto
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Precio como decimal (máximo 10 dígitos, con 2 decimales)
    marca = models.CharField(max_length=100)  # Marca como texto

    def __str__(self):
        return self.id_producto  # Mostrar el nombre del producto como representación del objeto
