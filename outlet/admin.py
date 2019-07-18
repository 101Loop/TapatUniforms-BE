from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin

from .models import Outlet, OutletProduct


class OutletAdmin(CreateUpdateAdmin):
    list_display = ('short_name', 'school',)
    list_filter = list_display


class OutletProductAdmin(CreateUpdateAdmin):
    list_display = ('outlet', 'product', 'price', 'image')
    list_filter = ('outlet', 'product')


admin.site.register(Outlet, OutletAdmin)
admin.site.register(OutletProduct, OutletProductAdmin)
