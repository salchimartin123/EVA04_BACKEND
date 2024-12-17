from django.contrib import admin
from reservasAPP.models import *

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre_reserva','telefono','fecha_reserva','hora_reserva','cantidad_personas','estado','observacion')

admin.site.register(Reserva, ReservaAdmin)

class EstadosAdmin(admin.ModelAdmin):
    list_display = ('estado',)

admin.site.register(reservaEstado, EstadosAdmin)