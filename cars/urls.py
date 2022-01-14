from django.urls import path

from cars.views import CarBrandList, CarModelList, UserCarList, CarBrandRetrieve, CarModelRetrieve, UserCarRetrieve

urlpatterns = [
    path('api/brands', CarBrandList.as_view()),
    path('api/brand/<int:pk>', CarBrandRetrieve.as_view()),
    path('api/models', CarModelList.as_view()),
    path('api/model/<int:pk>', CarModelRetrieve.as_view()),
    path('api/cars', UserCarList.as_view()),
    path('api/car/<int:pk>', UserCarRetrieve.as_view()),
]