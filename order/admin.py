from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin, CreateUpdateExcludeInlineAdminMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
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


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = (
            "id",
            "outlet__school__name",
            "create_date",
            "created_by__name",
            "name",
            "email",
        )
        export_order = ("id", "outlet__school__name", "create_date", "name", "email")


class TransactionInline(CreateUpdateExcludeInlineAdminMixin, admin.TabularInline):
    model = Transaction
    extra = 0


class SubOrderInline(CreateUpdateExcludeInlineAdminMixin, admin.TabularInline):
    model = SubOrder
    extra = 0


class OrderAdmin(ReadOnlyAdmin, ImportExportModelAdmin):
    inlines = [SubOrderInline, TransactionInline]
    list_display = ("order_id", "outlet", "name", "mobile", "email")
    list_filter = ("outlet__school__name",)
    search_fields = ("order_id", "mobile")
    ordering = ["id"]
    list_per_page = 50
    resource_class = OrderResource
    # actions = [export_to_csv]


@admin.register(Discount)
class DiscountAdmin(CreateUpdateAdmin):
    list_display = ("id", "discount_type", "value")
    ordering = ["id"]


admin.site.register(Order, OrderAdmin)
