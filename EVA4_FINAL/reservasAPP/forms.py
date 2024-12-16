from django import forms
from reservasAPP.models import Reserva

#clase para editar reserva
class ReservaRegistroForm(forms.Form):
    nombre_reserva = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=50)
    fecha_reserva = forms.DateField()
    hora_reserva = forms.TimeField()
    cantidad_personas = forms.IntegerField()
    estado = forms.CharField(max_length=50)
    observacion = forms.CharField(max_length=50)

    nombre_reserva.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    fecha_reserva.widget.attrs['class'] = 'form-control'
    hora_reserva.widget.attrs['class'] = 'form-control'
    cantidad_personas.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    observacion.widget.attrs['class'] = 'form-control'


# clase para validar reserva

class ReservaRegistroForm(forms.ModelForm):
    nombre_reserva = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=50)
    fecha_reserva = forms.DateField()
    hora_reserva = forms.TimeField()
    cantidad_personas = forms.IntegerField()
    estado = forms.CharField(max_length=50)
    observacion = forms.CharField(max_length=50)

    nombre_reserva.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    fecha_reserva.widget.attrs['class'] = 'form-control'
    hora_reserva.widget.attrs['class'] = 'form-control'
    cantidad_personas.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    observacion.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Reserva
        fields = '__all__'