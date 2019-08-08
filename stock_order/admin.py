from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin

from .models import IndentRequest, Indent, BoxItem, Box


class BoxItemInline(admin.TabularInline):
    extra = 1
    model = BoxItem


class BoxItemAdmin(CreateUpdateAdmin):
    inlines = (BoxItemInline, )


admin.site.register(Indent)
admin.site.register(IndentRequest)
admin.site.register(Box, BoxItemAdmin)

