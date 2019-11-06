from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin, CreateUpdateExcludeInlineAdminMixin

from .models import Discount, Order, SubOrder, Transaction


class TransactionInline(CreateUpdateExcludeInlineAdminMixin, admin.TabularInline):
    model = Transaction
    extra = 1


class SubOrderInline(CreateUpdateExcludeInlineAdminMixin, admin.TabularInline):
    model = SubOrder
    extra = 1


class OrderAdmin(CreateUpdateAdmin):
    inlines = [SubOrderInline, TransactionInline]
    list_display = ("order_id", "name", "mobile", "email", "discount", "outlet")
    list_filter = ("name", "mobile", "email")
    search_fields = ("name", "mobile")
    ordering = ["id"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Discount)
class DiscountAdmin(CreateUpdateAdmin):
    list_display = ("id", "discount_type", "value")
    ordering = ["id"]


admin.site.register(Order, OrderAdmin)
