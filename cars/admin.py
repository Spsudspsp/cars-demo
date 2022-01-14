from django.contrib import admin

# Register your models here.
from cars.models import CarBrand, CarModel, UserCar

admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(UserCar)