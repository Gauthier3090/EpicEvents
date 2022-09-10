from django.urls import path
from .views import ClientsCreateAndList, ClientDetail

urlpatterns = [
    path('', ClientsCreateAndList.as_view(), name='list'),
    path('<int:pk>/detail', ClientDetail.as_view(), name='details'),
]
