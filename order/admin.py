from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin, CreateUpdateExcludeInlineAdminMixin
import csv
import datetime
from django.http import HttpResponse
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


# def export_to_csv(modeladmin, request, queryset):
#     opts = modeladmin.model._meta
#     response = HttpResponse(content_type="text/csv")
#     response["Content-Disposition"] = "attachment;filename={}.csv".format(
#         opts.verbose_name
#     )
#     writer = csv.writer(response)
#     fields = [
#         field
#         for field in opts.get_fields()
#         if not field.many_to_many and not field.one_to_many
#     ]
#     # Write a first row with header information
#     writer.writerow([field.verbose_name for field in fields])
#     # Write data rows
#     for obj in queryset:
#         data_row = []
#         for field in fields:
#             value = getattr(obj, field.name)
#             if isinstance(value, datetime.datetime):
#                 value = value.strftime("%d/%m/%Y")
#             data_row.append(value)
#         writer.writerow(data_row)
#     return response
#
#
# export_to_csv.short_description = "Export to CSV"


class TransactionInline(CreateUpdateExcludeInlineAdminMixin, admin.TabularInline):
    model = Transaction
    extra = 0


class SubOrderInline(CreateUpdateExcludeInlineAdminMixin, admin.TabularInline):
    model = SubOrder
    extra = 0


class OrderAdmin(ReadOnlyAdmin):
    inlines = [SubOrderInline, TransactionInline]
    list_display = ("order_id", "outlet", "name", "mobile", "email")
    list_filter = ("outlet__school__name",)
    search_fields = ("order_id", "mobile")
    ordering = ["id"]
    list_per_page = 50
    # actions = [export_to_csv]


@admin.register(Discount)
class DiscountAdmin(CreateUpdateAdmin):
    list_display = ("id", "discount_type", "value")
    ordering = ["id"]


admin.site.register(Order, OrderAdmin)
