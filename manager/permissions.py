from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if obj._meta.model_name == "school":
            return obj._meta.model.objects.filter(
                outlet__manager__user=request.user, pk=obj.pk
            ).exists()

        return super().has_object_permission(request, view, obj)
