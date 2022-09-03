from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('clients/', views.ClientList.as_view(), name='client_list'),
    path('clients/<int:pk>/detail', views.ClientList.as_view(), name='client_detail'),
    path("contracts/", views.ContractList.as_view(), name="list"),
    path("contracts/<int:pk>/detail", views.ContractDetail.as_view(), name="detail"),
    path("events/", views.EventList.as_view(), name="event_list"),
    path("events/<int:pk>/detail", views.EventDetail.as_view(), name="event_detail"),
]
