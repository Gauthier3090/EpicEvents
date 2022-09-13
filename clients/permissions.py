from rest_framework import permissions
from users.models import SALES, SUPPORT
from .models import Client


class ClientPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team.name == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        return request.user.team.name == SALES

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return request.user.team.name == SALES and obj.status is False
        elif request.user.team.name == SUPPORT:
            return obj in Client.objects.filter(contract__event__support_contact=request.user)
        return request.user == obj.sales_contact or obj.status is False
