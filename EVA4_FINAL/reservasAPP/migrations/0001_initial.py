# Generated by Django 5.0.1 on 2024-12-15 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_reserva', models.CharField(max_length=50)),
                ('fecha_reserva', models.DateField()),
                ('hora_reserva', models.TimeField()),
                ('canitdad_personas', models.IntegerField()),
                ('observacion', models.CharField(max_length=50)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservasAPP.estadoreserva')),
            ],
        ),
    ]
