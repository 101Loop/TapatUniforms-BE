from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin

from .models import IndentRequest, Indent, BoxItem, Box


class BoxItemInline(admin.TabularInline):
    extra = 1
    model = BoxItem


class BoxItemAdmin(CreateUpdateAdmin):
    inlines = (BoxItemInline,)


class IndentAdmin(CreateUpdateAdmin):
    list_display = ("name", "price", "shipped_on")
    list_filter = ("name", "school")


admin.site.register(Indent, IndentAdmin)
admin.site.register(IndentRequest)
admin.site.register(Box, BoxItemAdmin)
