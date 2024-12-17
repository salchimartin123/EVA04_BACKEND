from django.db import models



class reservaEstado(models.Model):
    estado = models.CharField(max_length=50)
    def __str__(self): return self.estado


class Reserva(models.Model):
    
    nombre_reserva = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.IntegerField()
    estado = models.ForeignKey(reservaEstado, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=50)

    def __str__(self): return 'Reserva'