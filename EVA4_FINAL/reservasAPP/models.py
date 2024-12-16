from django.db import models

# Create your models here.

class Reserva(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_reserva = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.IntegerField()
    estado = models.CharField(max_length=50)
    observacion = models.CharField(max_length=50)