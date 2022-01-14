from django.urls import path

from accounts.views import UserList, UserRetrieve, UserRegister, LoginView, LogoutView

urlpatterns = [
    path('api/users', UserList.as_view()),
    path('api/users/login', LoginView.as_view()),
    path('api/users/logout', LogoutView.as_view()),
    path('api/users/<int:pk>', UserRetrieve.as_view()),
    path('api/users/register', UserRegister.as_view())
]