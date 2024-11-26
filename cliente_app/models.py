from django.db import models


class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=6)  # ID único para el cliente
    nombre = models.CharField(max_length=50)  # Para almacenar nombres como texto
    apellido = models.CharField(max_length=50)  # Para almacenar apellidos como texto
    email = models.CharField(max_length=100)  # Campo para direcciones de correo electrónico, validado
    telefono = models.CharField(max_length=15, blank=True, null=True)  # Para números de teléfono (posible prefijo + dígitos)
    direccion = models.TextField(blank=True, null=True)  # Para direcciones completas como texto

    def __str__(self):
        return self.id_cliente
