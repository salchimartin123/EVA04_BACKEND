from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from reservasAPP.models import Reserva
from reservasAPP.serializers import ReservaSerializer
from rest_framework.response import Response
from rest_framework import status
from reservasAPP.serializers import ValidacionReserva
from rest_framework.views import APIView
from django.db import IntegrityError
from reservasAPP.forms import *

#clase para mostrar index
def index(request):
    return render(request, 'index.html')

##reservas en datatable
def listadereservas(request):
    reservas = Reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservastemplates/reservas.html', data)

def reservaRegistro(request):
    form = ReservaRegistroForm()
    
    if request.method == 'POST':
        form = ReservaRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listadereservas'))
            
    data = {'form':form}
    return render(request, 'reservastemplates/reservasregistro.html',data)

def reservaEliminar(request,id):
    empleado = Reserva.objects.get(id=id)
    empleado.delete()
    return HttpResponseRedirect(reverse('listadereservas'))

def reservaEditar(request, id):
    empleado = Reserva.objects.get(id=id)
    form = ReservaRegistroForm(instance=empleado)
    
    if request.method == 'POST':
        form = ReservaRegistroForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listadereservas'))
            
    data = {'form':form} 
    return render(request, 'reservastemplates/reservasregistro.html', data)








#Clases para Reservas desde API
###############################

class ReservaList(APIView):
    def get(self, request):
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ValidacionReserva(data=request.data)
        
        if serializer.is_valid():
            reserva_data = serializer.validated_data
            reserva_id = reserva_data.get('id')

            if Reserva.objects.filter(id=reserva_id).exists():
                return Response({"error": f"Ya existe una reserva con la ID {reserva_id}."}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                
                reserva = Reserva.objects.create(**reserva_data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                
                return Response({"error": "Hubo un error al guardar la reserva."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Reservadetail(APIView):

    def get_object(self, pk):
        try:
            return Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            return None

    def get(self, request, pk):
        reserva = self.get_object(pk)
        if reserva is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data)

    def put(self, request, pk):
        reserva = self.get_object(pk)
        if reserva is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reserva = self.get_object(pk)
        if reserva is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
