# Generated by Django 5.1.3 on 2024-11-26 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='horario',
            field=models.CharField(max_length=100),
        ),
    ]