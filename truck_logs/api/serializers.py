from rest_framework import serializers

from logbook.models import Truck, Shipment
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
        )


class TruckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Truck
        fields = (
            'truck_no',
        )


class ShipmentPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipment
        fields = (
            'person_responsible',
            'truck_no',
            'departure_point',
            'destination_point',
            'departure_date',
            'arrival_date',
            'truck_actual_arrival_time_departure_point',
            'truck_actual_departure_time_departure_point',
            'truck_actual_arrival_time_destination_point',
            'truck_actual_departure_time_destination_point',
            'techincal_check',
            'unplanend_repairs',
            'overload',
            'overheating',
        )


class ShipmentGetSerializer(serializers.ModelSerializer):
    truck_no = serializers.StringRelatedField(read_only=True)
    person_responsible = serializers.StringRelatedField(read_only=True, source='person_responsible.first_name')

    class Meta:
        model = Shipment
        fields = (
            'id',
            'person_responsible',
            'truck_no',
            'departure_point',
            'destination_point',
            'departure_date',
            'arrival_date',
            'truck_actual_arrival_time_departure_point',
            'truck_actual_departure_time_departure_point',
            'truck_actual_arrival_time_destination_point',
            'truck_actual_departure_time_destination_point',
            'techincal_check',
            'unplanend_repairs',
            'overload',
            'overheating',
        )
