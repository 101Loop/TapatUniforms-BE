from rest_framework import filters
import django_filters
from outlet.models import Outlet


class IsManagerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their objects related to specific outlet.
    """

    def filter_queryset(self, request, queryset, view):
        if queryset.model._meta.model_name == "school":
            return queryset.filter(outlet__manager__user=request.user)

        elif queryset.model._meta.model_name == "student":
            return queryset.filter(school__outlet__manager__user=request.user)

        else:
            raise ValueError("Unsupported model applied in filter.")
