from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin, CreateUpdateExcludeInlineAdminMixin

from .models import Order, SubOrder, Transaction, Discount


class TransactionInline(CreateUpdateExcludeInlineAdminMixin, admin.TabularInline):
    model = Transaction
    extra = 1


class SubOrderInline(CreateUpdateExcludeInlineAdminMixin, admin.TabularInline):
    model = SubOrder
    extra = 1


class OrderAdmin(CreateUpdateAdmin):
    inlines = [SubOrderInline, TransactionInline]
    list_display = ("name", "mobile", "email", "discount", "outlet")
    list_filter = ("name", "mobile", "email")
    search_fields = ("name", "mobile")


@admin.register(Discount)
class DiscountAdmin(CreateUpdateAdmin):
    list_display = ("id", "discount_type", "value")
    ordering = ["id"]


admin.site.register(Order, OrderAdmin)
