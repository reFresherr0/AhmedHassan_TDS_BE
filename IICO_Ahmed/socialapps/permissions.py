from  rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminCurrentUser(BasePermission):
        SAFE_METHODS = ['GET']
        def has_permission(self, request, view):
            return (request.user.is_authenticated or request.user.is_superuser or request.method in SAFE_METHODS)

        def has_object_permission(self, request, view, obj):
             return obj.user_id == request.user or request.user.is_superuser