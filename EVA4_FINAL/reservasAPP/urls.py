from django.contrib import admin
from django.urls import path
from reservasAPP.views import *


urlpatterns = [
    
    

    #paths para API

    #path('reservasAPI/', reservas_list),
    #path('reservasAPI/<int:pk>/', reservas_detail),
    path('listadereservas/', listadereservas, name='listadereservas'),
    path('cReservasAPI/', ReservaList.as_view(), name='cReservasAPI'),
    path('cReservasAPI/<int:pk>/', Reservadetail.as_view()),

    #paths para datatable
    path('reservaRegistro/', reservaRegistro, name='reservaregistro'),
    path('reservaEliminar/<int:id>', reservaEliminar, name='reservaeliminar'),
    path('reservaEditar/<int:id>', reservaEditar, name='reservaeditar'),
    
]
