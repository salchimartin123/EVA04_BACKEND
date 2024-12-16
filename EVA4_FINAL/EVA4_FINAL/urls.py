from django.contrib import admin
from django.urls import path
from reservasAPP.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='home'),
    #path('reservasAPI/', reservas_list),
    #path('reservasAPI/<int:pk>/', reservas_detail),
    path('listadereservas/', listadereservas, name='listadereservas'),
    path('cReservasAPI/', ReservaList.as_view(), name='cReservasAPI'),
    path('cReservasAPI/<int:pk>/', Reservadetail.as_view()),
]
