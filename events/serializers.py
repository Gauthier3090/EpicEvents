from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only__fields = ['date_created', 'date_updated', 'support_contact', 'event_status', 'id']
        extra_kwargs = {
            'name': {'required': True},
            'location': {'required': True},
            'attendees': {'required': True},
            'event_date': {'required': True},
            'contract': {'required': True},
            'support_contact': {'required': False},
            'event_status': {'required': False},
            'status': {'required': False}
        }
