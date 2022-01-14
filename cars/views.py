from datetime import datetime

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from cars.filters import CarBrandFilter, CarModelFilter, UserCarFilter
from cars.models import CarBrand, CarModel, UserCar
from cars.serializers import CarBrandSerializer, CarModelSerializer, UserCarSerializer

from django_filters import rest_framework as filters


class CarBrandList(ListCreateAPIView):
    serializer_class = CarBrandSerializer
    queryset = CarBrand.objects.filter(deleted_at__isnull=True)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CarBrandFilter


class CarBrandRetrieve(RetrieveDestroyAPIView):
    serializer_class = CarBrandSerializer
    queryset = CarBrand.objects.filter(deleted_at__isnull=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = datetime.now()
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarModelList(ListCreateAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.filter(deleted_at__isnull=True)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CarModelFilter


class CarModelRetrieve(RetrieveUpdateDestroyAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.filter(deleted_at__isnull=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = datetime.now()
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCarList(ListCreateAPIView):
    serializer_class = UserCarSerializer
    queryset = UserCar.objects.filter(deleted_at__isnull=True)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserCarFilter


class UserCarRetrieve(RetrieveDestroyAPIView):
    serializer_class = UserCarSerializer
    queryset = UserCar.objects.filter(deleted_at__isnull=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = datetime.now()
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)