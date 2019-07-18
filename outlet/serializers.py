from rest_framework import serializers


class OutletSerializer(serializers.ModelSerializer):
    from school.serializers import SchoolSerializer

    school = SchoolSerializer(many=False)

    class Meta:
        from .models import Outlet

        model = Outlet
        fields = ('id', 'school', 'short_name')
        read_only_fields = fields


class OutletProductSerializer(serializers.ModelSerializer):
    from product.serializers import ProductSerializer

    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        from .models import OutletProduct

        model = OutletProduct
        fields = ('id', 'price', 'image', 'outlet', 'product', 'color',
                  'color_code', 'size', 'warehouse_stock', 'display_stock')
        read_only_fields = fields
