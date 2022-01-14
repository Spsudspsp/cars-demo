from rest_framework import serializers

from cars.models import CarBrand, CarModel, UserCar


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ['id', 'name', 'created_at']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'car_brand', 'name', 'created_at', 'updated_at']


class UserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = ['id', 'user', 'car_brand', 'car_model', 'first_reg', 'odo', 'created_at']