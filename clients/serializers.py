from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        read_only__fields = ['date_created', 'date_updated', 'sales_contact', 'id']
        extra_kwargs = {
            'firstname': {'required': True},
            'lastname': {'required': True},
            'email': {'required': True},
            'phone': {'required': False},
            'mobile': {'required': False},
            'company_name': {'required': True},
            'sales_contact': {'required': False},
            'status': {'required': False}
        }
