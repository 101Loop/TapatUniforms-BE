from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and
                    request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        # ToDo: something needs to be done here
        return super().has_object_permission(request, view, obj)

