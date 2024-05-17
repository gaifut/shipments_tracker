from rest_framework import viewsets
from djoser.views import UserViewSet
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.permissions import AllowAny

from logbook.models import Truck, Shipment
# from users.models import User
from .serializers import (
    CustomUserSerializer, TruckSerializer,
    ShipmentGetSerializer, ShipmentPostSerializer
)


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)


class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    permission_classes = (AllowAny,)


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ShipmentGetSerializer
        return ShipmentPostSerializer

    def list(self, request, *args, **kwargs):
        shipments = self.get_queryset()
        unique_dates = sorted(
            set(shipments.values_list(
                    'arrival_date', flat=True)))
        context = {
            'shipments': shipments,
            'unique_dates': unique_dates,
        }
        return render(
            request, 'shipment_calendar.html', context
        )


class LogbookShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ShipmentGetSerializer
        return ShipmentPostSerializer

    def list(self, request, *args, **kwargs):
        shipments = self.get_queryset()
        unique_dates = sorted(
            set(shipments.values_list(
                    'arrival_date', flat=True)))
        context = {
            'shipments': shipments,
            'unique_dates': unique_dates,
        }
        return render(
            request, 'logbook.html', context
        )
