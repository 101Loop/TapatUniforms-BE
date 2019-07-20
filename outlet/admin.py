from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin

from .models import Outlet, OutletProduct, OutletSubProduct


class OutletAdmin(CreateUpdateAdmin):
    list_display = ('short_name', 'school',)
    list_filter = list_display


class ProductInline(admin.TabularInline):
    extra = 1
    model = OutletSubProduct


class OutletProductAdmin(CreateUpdateAdmin):
    inlines = (ProductInline, )
    list_display = ('outlet', 'product', 'image')
    list_filter = ('outlet', 'product')


admin.site.register(Outlet, OutletAdmin)
admin.site.register(OutletProduct, OutletProductAdmin)
