from rest_framework import permissions


class CustomUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        elif view.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated
        return False

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated and request.user == obj
        return False
