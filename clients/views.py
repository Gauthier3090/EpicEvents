from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.permissions import IsManager
from users.models import SALES, SUPPORT
from .models import Client
from .permissions import ClientPermissions
from .serializers import ClientSerializer


class ClientsCreateAndList(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, ClientPermissions | IsManager]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["lastname", "email"]

    def get_queryset(self):
        if self.request.user.team == SUPPORT:
            return Client.objects.filter(
                contract__event__support_contact=self.request.user
            ).distinct()
        elif self.request.user.team == SALES:
            clients_status_false = Client.objects.filter(status=False)
            own = Client.objects.filter(sales_contact=self.request.user)
            return clients_status_false | own
        return Client.objects.all()

    def post(self, request, *args, **kwargs):
        if Client.objects.filter(email=self.request.data['email']).exists():
            return Response({"error": "This client already exists."})
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data["status"] is True:
                serializer.validated_data["sales_contact"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    http_method_names = ["get", "put", "delete", "options"]
    permission_classes = [IsAuthenticated, IsManager | ClientPermissions]
    serializer_class = ClientSerializer

    def update(self, request, *args, **kwargs):
        client = self.get_object()
        serializer = ClientSerializer(data=request.data, instance=client)
        if serializer.is_valid(raise_exception=True):
            if client.status is True and serializer.validated_data["status"] is False:
                raise ValidationError(
                    {"detail": "Cannot change status of converted client."}
                )
            elif serializer.validated_data["status"] is True:
                serializer.validated_data["sales_contact"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
