from django.db import models

# Create your models here.


class Person(models.Model):
  # first_name = models.CharField(max_length=64)
  # last_name = models.CharField(max_length=64)
  # email = models.CharField(max_length=64)
  # origination_city = models.CharField(max_length=64)
  # origination_state = models.CharField(max_length=2)
  # destination_city = models.CharField(max_length=64)
  # destination_state = models.CharField(max_length=2)
  # vehicle_type = models.CharField(max_length=64)
  # premium = models.CharField(max_length=1)
  # date = models.DateField()
  # taking_passengers = models.BooleanField(default=False)
  # seats_available = models.IntegerField(default=0)


  first_name = models.CharField(max_length=64)
  X_acceleration = models.DecimalField(max_digits=64, decimal_places=64, default = 0.0)
  Y_acceleration = models.DecimalField(max_digits=64, decimal_places=64, default = 0.0)
  Z_acceleration = models.DecimalField(max_digits=64, decimal_places=64, default = 0.0)
  X_gyroscope = models.DecimalField(max_digits=64, decimal_places=64, default = 0.0)
  Y_gyroscope = models.DecimalField(max_digits=64, decimal_places=64, default = 0.0)
  Z_gyroscope = models.DecimalField(max_digits=64, decimal_places=64, default = 0.0)