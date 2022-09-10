from rest_framework import permissions
from .models import MANAGEMENT


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        print(permissions.SAFE_METHODS, request.method, request.user.team)
        return request.user.team == MANAGEMENT and request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
