from django.contrib import admin

from drfaddons.admin import CreateUpdateAdmin

from .models import CategoryMaster, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(CreateUpdateAdmin):
    fieldsets = (
    )
    inlines = [ProductImageInline, ]
    list_display = ('name', 'price', 'sku')
    list_filter = ('price', 'sku')
    search_fields = ('name', 'sku')


admin.site.register(CategoryMaster)
admin.site.register(Product, ProductAdmin)
