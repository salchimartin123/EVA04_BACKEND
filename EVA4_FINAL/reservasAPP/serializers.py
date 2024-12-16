from rest_framework import serializers
from reservasAPP.models import Reserva
from django.core.exceptions import ValidationError

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'


class ValidacionReserva(serializers.Serializer):
    id = serializers.IntegerField()
    nombre_reserva = serializers.CharField(max_length=50)
    telefono = serializers.CharField(max_length=50)
    fecha_reserva = serializers.DateField()
    hora_reserva = serializers.TimeField()
    cantidad_personas = serializers.IntegerField()
    estado = serializers.CharField(max_length=50)
    observacion = serializers.CharField(max_length=50, required=False)

    def validate_cantidad_personas(self, value):
        # Validación de que la cantidad de personas esté entre 1 y 15
        if value < 1 or value > 15:
            raise ValidationError("La cantidad de personas debe estar entre 1 y 15.")
        return value
