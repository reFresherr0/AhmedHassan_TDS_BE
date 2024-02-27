from  rest_framework.permissions import BasePermission


class IsTdsMember(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.tds_member)