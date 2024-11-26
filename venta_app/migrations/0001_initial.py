# Generated by Django 5.1.3 on 2024-11-19 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('estado', models.CharField(max_length=50)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_producto', models.TextField(blank=True, null=True)),
                ('id_empleado', models.CharField(blank=True, max_length=10, null=True)),
                ('id_cliente', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]