from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from .models import Garage, Client, Service, Scheduler, CarMechanic

from api.serializers import UserSerializer, GarageSerializer, ClientSerializer, ServiceSerializer, SchedulerSerializer, CarMechanicSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GarageViewSet(viewsets.ModelViewSet):
    serializer_class = GarageSerializer

    def get_queryset(self):
        house_number = self.request.query_params.get('house_number', None)
        garage = Garage.objects.filter(house_number=house_number)
        return garage

    # def list(self, request, *args, **kwargs):
    #     name_garage = self.request.query_params.get('name_garage', None)
    #     garage = Garage.objects.filter(name_garage__exact=name_garage)
    #     return garage


class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ServiceViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SchedulerViewSet(viewsets.ModelViewSet):

    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerializer


class CarMechanicViewSet(viewsets.ModelViewSet):

    queryset = CarMechanic.objects.all()
    serializer_class = CarMechanicSerializer
