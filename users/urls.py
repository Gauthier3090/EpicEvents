from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import PasswordUpdate

app_name = 'user'
urlpatterns = (
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('password-update/', PasswordUpdate.as_view(), name='password_update'),
)
