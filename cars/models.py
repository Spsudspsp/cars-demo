from django.db import models

from accounts.models import CustomUser


class CarBrand(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=10)
    deleted_at = models.DateTimeField(null=True, blank=True)


class CarModel(models.Model):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class UserCar(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.DO_NOTHING)
    car_model = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING)
    first_reg = models.DateTimeField()
    odo = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)