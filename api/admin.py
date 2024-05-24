from django.contrib import admin
from .models import Garage, Client, Service, Scheduler, CarMechanic

# Register your models here.

admin.site.register(Garage)
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Scheduler)
admin.site.register(CarMechanic)
