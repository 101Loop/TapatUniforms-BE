from rest_framework import serializers


class OutletSerializer(serializers.ModelSerializer):
    from school.serializers import SchoolSerializer

    school = SchoolSerializer(many=False)

    class Meta:
        from .models import Outlet

        model = Outlet
        fields = ("id", "school", "short_name")
        read_only_fields = fields


class LProductSerializer(serializers.ModelSerializer):
    from product.serializers import ProductSerializer

    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        from .models import OutletProduct

        model = OutletProduct
        fields = ("id", "name", "image", "outlet", "product", "color", "color_code")


class OutletSubProductSerializer(serializers.ModelSerializer):
    outlet_product = LProductSerializer(many=False)

    class Meta:
        from .models import OutletSubProduct

        model = OutletSubProduct
        fields = (
            "id",
            "outlet_product",
            "size",
            "price",
            "warehouse_stock",
            "display_stock",
        )


class ManageSubProductSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import OutletSubProduct

        model = OutletSubProduct
        fields = ("id", "warehouse_stock", "display_stock")


class OutletProductSerializer(serializers.ModelSerializer):
    from product.serializers import ProductSerializer

    product = ProductSerializer(many=False, read_only=True)
    outletsubproduct_set = OutletSubProductSerializer(many=True)

    class Meta:
        from .models import OutletProduct

        model = OutletProduct
        fields = (
            "id",
            "name",
            "outletsubproduct_set",
            "image",
            "outlet",
            "product",
            "color",
            "color_code",
        )
