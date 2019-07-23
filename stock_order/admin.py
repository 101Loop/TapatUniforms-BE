from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin

from .models import IndentRequestDetail, IndentRequest, Indent, BoxItem, Box


class BoxItemInline(admin.TabularInline):
    extra = 1
    model = BoxItem


class IndentRequestDetailInline(admin.TabularInline):
    extra = 1
    model = IndentRequestDetail


class IndentRequestDetailAdmin(CreateUpdateAdmin):
    inlines = (IndentRequestDetailInline, )


class BoxItemAdmin(CreateUpdateAdmin):
    inlines = (BoxItemInline, )


admin.site.register(Indent)
admin.site.register(IndentRequest, IndentRequestDetailAdmin)
admin.site.register(Box, BoxItemAdmin)

