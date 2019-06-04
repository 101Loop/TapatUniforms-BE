from rest_framework import serializers


class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Outlet

        model = Outlet
        fields = ('id', 'name',)
        read_only_fields = fields


class OutletProductSerializer(serializers.ModelSerializer):
    from product.serializers import ProductSerializer

    outlet = OutletSerializer(many=False, read_only=True)
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        from .models import OutletProduct

        model = OutletProduct
        fields = ('id', 'outlet', 'product')
        read_only_fields = fields
