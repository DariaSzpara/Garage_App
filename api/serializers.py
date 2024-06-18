from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Garage, Client, Service, Scheduler, CarMechanic


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = [
            "id",
            "name_garage",
            "adress_city_name",
            "street_name",
            "house_number",
            "postal_code",
        ]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "name_client",
            "last_name_client",
            "email",
            "adress_city_name",
            "street_name",
            "house_number",
            "postal_code",
            "number_phone",
        ]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name_of_service", "price", "status_paid"]


class SchedulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduler
        fields = ["id", "date"]


class CarMechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMechanic
        fields = ["id", "first_name", "last_name", "number_phone"]
