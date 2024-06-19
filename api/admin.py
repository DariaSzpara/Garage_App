from django.contrib import admin

from .models import CarMechanic, Client, Garage, Scheduler, Service


# Register your models here.
class GarageAdmin(admin.ModelAdmin):
    list_display = ("id", "name_garage")


class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "name_client", "last_name_client", "email")
    search_fields = ("name_client",)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name_of_service", "price", "status_paid")
    list_filter = ["status_paid"]


class SchedulerAdmin(admin.ModelAdmin):
    list_display = ("id", "date")
    date_hierarchy = "date"


admin.site.register(Garage, GarageAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Scheduler, SchedulerAdmin)
admin.site.register(CarMechanic)
