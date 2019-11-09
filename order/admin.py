from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin, CreateUpdateExcludeInlineAdminMixin

from .models import Discount, Order, SubOrder, Transaction


class ReadOnlyAdmin(CreateUpdateAdmin):
    """Provides a read-only view of a model in Django admin."""

    # readonly_fields = []

    def change_view(self, request, object_id, extra_context=None):
        """ customize add/edit form to remove save / save and continue """
        extra_context = extra_context or {}
        extra_context["show_save_and_continue"] = False
        extra_context["show_save"] = False
        return super().change_view(request, object_id, extra_context=extra_context)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def get_readonly_fields(self, request, obj=None):
        return (
            list(self.readonly_fields)
            + [field.name for field in obj._meta.fields]
            + [field.name for field in obj._meta.many_to_many]
        )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TransactionInline(CreateUpdateExcludeInlineAdminMixin, admin.TabularInline):
    model = Transaction
    extra = 1


class SubOrderInline(CreateUpdateExcludeInlineAdminMixin, admin.TabularInline):
    model = SubOrder
    extra = 1


class OrderAdmin(ReadOnlyAdmin):
    inlines = [SubOrderInline, TransactionInline]
    list_display = ("order_id", "name", "mobile", "email", "discount", "outlet")
    list_filter = ("name", "mobile", "email")
    search_fields = ("name", "mobile")
    ordering = ["id"]


@admin.register(Discount)
class DiscountAdmin(CreateUpdateAdmin):
    list_display = ("id", "discount_type", "value")
    ordering = ["id"]


admin.site.register(Order, OrderAdmin)
