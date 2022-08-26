from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('clients/', views.ClientList.as_view(), name='client_list'),
]
