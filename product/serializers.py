from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import CategoryMaster

        model = CategoryMaster
        fields = ('id', 'name', 'image')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Product

        model = Product
        fields = ('id', 'name', 'sku', 'category', 'gender_type',
                  'product_type')
        read_only_field = fields
