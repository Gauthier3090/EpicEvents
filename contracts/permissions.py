from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from users.models import SUPPORT, SALES
from .models import Client, Contract


class ContractPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team.name == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        return request.user.team.name == SALES

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.user.team.name == SUPPORT:
                return obj in Contract.objects.filter(
                    event__support_contact=request.user
                )
            return request.user == obj.sales_contact
        elif request.method == "PUT" and obj.status is True:
            raise PermissionDenied("Cannot update a signed contract.")
        return request.user == obj.sales_contact and obj.status is False
