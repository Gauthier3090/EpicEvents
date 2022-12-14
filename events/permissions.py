from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from users.models import SALES, SUPPORT


class EventPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team.name == SUPPORT:
            return request.method in ["GET", "PUT"]
        return request.user.team.name == SALES

    def has_object_permission(self, request, view, obj):
        if obj.event_status is True:
            raise PermissionDenied("Cannot update a finished event.")
        if request.method in permissions.SAFE_METHODS:
            return (
                request.user == obj.support_contact
                or request.user == obj.contract.sales_contact
            )
        else:
            if request.user.team.name == SUPPORT:
                return request.user == obj.support_contact
            return request.user == obj.contract.sales_contact
