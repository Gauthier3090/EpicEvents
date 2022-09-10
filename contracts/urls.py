from django.urls import path
from .views import ContractsCreateAndList, ContractDetail

urlpatterns = [
    path('', ContractsCreateAndList.as_view(), name='list'),
    path('<int:pk>/detail', ContractDetail.as_view(), name='details'),
]
