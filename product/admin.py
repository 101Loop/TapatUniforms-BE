from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin
from .models import CategoryMaster, Product


class CategoryAdmin(CreateUpdateAdmin):
    list_display = ('name',)
    search_fields = list_display


class ProductAdmin(CreateUpdateAdmin):
    list_display = ('name', 'sku')
    search_fields = ('name',)


admin.site.register(CategoryMaster, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
