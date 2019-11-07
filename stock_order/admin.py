from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin, CreateUpdateExcludeInlineAdminMixin

from .models import Box, BoxItem, Indent, IndentRequest


class BoxItemInline(CreateUpdateExcludeInlineAdminMixin, admin.TabularInline):
    extra = 0
    model = BoxItem
    readonly_fields = ("item_scanned", "warehouse_stock")


class BoxItemAdmin(CreateUpdateAdmin):
    inlines = (BoxItemInline,)


class IndentAdmin(CreateUpdateAdmin):
    list_display = ("indent_name", "price", "warehouse_name", "shipped_on")
    list_filter = ("indent_name",)


@admin.register(IndentRequest)
class IndentRequestAdmin(CreateUpdateAdmin):
    list_display = ("id", "product", "outlet", "requested_on")


admin.site.register(Indent, IndentAdmin)

admin.site.register(Box, BoxItemAdmin)
