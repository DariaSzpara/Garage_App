from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Garage(models.Model):
    name_garage = models.CharField(max_length=55)
    adress_city_name = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    house_number = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=6,
                                   validators=[RegexValidator('^[0-9]{2}-[0-9]{3}')])


class Client(models.Model):
    name_client = models.CharField(max_length=20)
    last_name_client = models.CharField(max_length=20)
    email = models.EmailField(
        max_length=254, unique=True, null=False, blank=False)
    adress_city_name = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    house_number = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=6,
                                   validators=[RegexValidator('^[0-9]{2}-[0-9]{3}')])
    number_phone = models.CharField(max_length=9, null=True, blank=True)


class Service(models.Model):
    # STATUS_PRICE = [
    #     ('UP', 'Unpaid'),
    #     ('P', 'Paid')
    # ]
    name_of_service = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # status_paid = models.CharField(max_length=2, choices=STATUS_PRICE)


class Scheduler(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)


class CarMechanic(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    number_phone = models.CharField(max_length=9, null=True, blank=True)
