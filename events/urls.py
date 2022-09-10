from django.urls import path
from .views import EventsCreateAndList, EventDetail

urlpatterns = [
    path('', EventsCreateAndList.as_view(), name='list'),
    path('<int:pk>/detail', EventDetail.as_view(), name='details'),
]
