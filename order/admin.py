from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin

from .models import Order, SubOrder, Transaction


class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 1


class SubOrderInline(admin.TabularInline):
    model = SubOrder
    extra = 1


class OrderAdmin(CreateUpdateAdmin):
    inlines = [SubOrderInline, TransactionInline]
    list_display = ('name', 'mobile', 'email', 'discount', 'outlet')
    list_filter = ('name', 'mobile', 'email')
    search_fields = ('name', 'mobile')


admin.site.register(Order, OrderAdmin)
