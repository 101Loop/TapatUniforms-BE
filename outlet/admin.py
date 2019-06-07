from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin

from .models import Outlet, OutletProduct


class OutletAdmin(CreateUpdateAdmin):
    list_display = ('name',)
    search_fields = list_display


class OutletProductAdmin(CreateUpdateAdmin):
    list_display = ('outlet', 'product', 'price', 'image')


admin.site.register(Outlet, OutletAdmin)
admin.site.register(OutletProduct, OutletProductAdmin)
