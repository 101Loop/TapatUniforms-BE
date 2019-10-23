from django.contrib import admin
from drfaddons.admin import CreateUpdateExcludeInlineAdminMixin, CreateUpdateAdmin
from location.models import State, City, WareHouse


class CityInline(CreateUpdateExcludeInlineAdminMixin, admin.StackedInline):
    extra = 0
    model = City


class StateAdmin(CreateUpdateAdmin):
    inlines = (CityInline,)
    list_display = ("id", "name")
    exclude = ()
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("id",)


@admin.register(WareHouse)
class WareHouseAdmin(CreateUpdateAdmin):
    list_display = ()


admin.site.register(State, StateAdmin)
# admin.site.register(WareHouse)
