from django.contrib.auth.models import User
from rest_framework import serializers

from .models import CarMechanic, Client, Garage, Scheduler, Service


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = __all__


class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = __all__


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = __all__


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = __all__


class SchedulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduler
        fields = __all__


class CarMechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMechanic
        fields = __all__
