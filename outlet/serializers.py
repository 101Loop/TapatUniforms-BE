from rest_framework import serializers


class OutletSerializer(serializers.ModelSerializer):
    from school.serializers import SchoolSerializer

    school = SchoolSerializer(many=False)

    class Meta:
        from .models import Outlet

        model = Outlet
        fields = ('id', 'school', 'short_name')
        read_only_fields = fields


class OutletSubProductSerializer(serializers.ModelSerializer):

    class Meta:
        from .models import OutletSubProduct

        model = OutletSubProduct
        fields = ('outlet_product', 'size', 'price', 'warehouse_stock', 'display_stock')


class OutletProductSerializer(serializers.ModelSerializer):
    from product.serializers import ProductSerializer

    product = ProductSerializer(many=False, read_only=True)
    outlet_sub_product_set = OutletSubProductSerializer(many=True)

    class Meta:
        from .models import OutletProduct

        model = OutletProduct
        fields = ('id', 'outlet_sub_product_set', 'image', 'outlet', 'product', 'color',
                  'color_code')
        read_only_fields = fields


