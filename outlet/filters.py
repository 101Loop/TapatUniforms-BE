from rest_framework import filters


class IsManagerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their objects related to specific outlet.
    """

    def filter_queryset(self, request, queryset, view):
        if queryset.model._meta.model_name == "outletproduct":
            return queryset.filter(outlet__manager__user=request.user)

        elif queryset.model._meta.model_name == "outlet":
            return queryset.filter(school__outlet__manager__user=request.user)
        elif queryset.model._meta.model_name == "outletsubproduct":
            return queryset.filter(outlet_product__outlet__manager__user=request.user)
        else:
            raise ValueError("Unsupported model applied in filter.")
