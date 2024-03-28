from rest_framework import permissions

class UserToPermission(permissions.BasePermission):
         message = 'You cannot access this notification.'

         def has_permission(self, request, view):
            return bool(request.user)


         def has_object_permission(self, request, view, obj):
            return obj.user_to == request.user or request.user.is_superuser