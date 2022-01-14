from django_filters import rest_framework as filters

from cars.models import CarBrand, CarModel, UserCar


class CarBrandFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = CarBrand
        fields = ['name']


class CarModelFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = CarModel
        fields = ['name']


class UserCarFilter(filters.FilterSet):
    odo = filters.NumberFilter()
    odo__gt = filters.NumberFilter(field_name='odo', lookup_expr='gt')
    odo__lt = filters.NumberFilter(field_name='odo', lookup_expr='lt')
    first_reg = filters.DateTimeFilter()

    class Meta:
        model = UserCar
        fields = ['odo', 'odo__gt', 'odo__lt', 'first_reg']
