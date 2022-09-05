from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import PasswordUpdate, CreateUser

urlpatterns = [
    path('signup/', CreateUser.as_view(), name='create'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('password-update/', PasswordUpdate.as_view(), name='password_update'),
]
