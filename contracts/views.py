from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.permissions import IsManager
from contracts.models import Contract
from contracts.permissions import ContractPermissions
from contracts.serializers import ContractSerializer
from users.models import SALES, SUPPORT


class ContractsCreateAndList(generics.ListCreateAPIView):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsManager | ContractPermissions]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        "client__lastname",
        "client__email",
        "date_created",
        "amount"
    ]

    def get_queryset(self):
        if self.request.user.team == SUPPORT:
            return Contract.objects.filter(event__support_contact=self.request.user)
        elif self.request.user.team == SALES:
            return Contract.objects.filter(sales_contact=self.request.user)
        return Contract.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = ContractSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data["sales_contact"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ContractDetail(generics.RetrieveUpdateAPIView):
    queryset = Contract.objects.all()
    http_method_names = ["get", "put", "options"]
    permission_classes = [IsAuthenticated, IsManager | ContractPermissions]
    serializer_class = ContractSerializer

    def update(self, request, *args, **kwargs):
        serializer = ContractSerializer(data=request.data, instance=self.get_object())
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data["sales_contact"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
