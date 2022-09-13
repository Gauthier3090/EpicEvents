from rest_framework import permissions
from .models import MANAGEMENT


class IsManager(permissions.BasePermission):
    permissions.SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS', 'POST', 'PUT', 'DELETE')

    def has_permission(self, request, view):
        return request.user.team.name == MANAGEMENT and request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
