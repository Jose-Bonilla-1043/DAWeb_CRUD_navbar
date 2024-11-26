from django.db import models


class Proveedor(models.Model):
    id_proveedor = models.CharField(primary_key=True, max_length=6)  # ID único para el proveedor
    nombre = models.CharField(max_length=100)  # El nombre debe ser texto, no un número
    contacto = models.CharField(max_length=50)  # Nombre o identificación del contacto, como texto
    telefono = models.CharField(max_length=15, blank=True, null=True)  # Número de teléfono con formato correcto
    direccion = models.CharField(max_length=100)  # Dirección como texto
    ciudad = models.CharField(max_length=50, blank=True, null=True)  # Ciudad como texto

    def __str__(self):
        return self.id_proveedor
