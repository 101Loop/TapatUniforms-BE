from rest_framework import serializers


class SubOrderSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import SubOrder

        model = SubOrder
        fields = ("order", "product", "price", "quantity", "total")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Order

        model = Order
        fields = ("id", "name", "mobile", "email", "discount", "outlet", "order_id")


class AllOrderSerializer(serializers.ModelSerializer):
    suborder_set = SubOrderSerializer(many=True)

    class Meta:
        from .models import Order

        model = Order
        fields = (
            "id",
            "name",
            "mobile",
            "email",
            "discount",
            "outlet",
            "order_id",
            "suborder_set",
        )


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Transaction

        model = Transaction
        fields = ("order", "amount", "mode")


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Discount

        model = Discount
        fields = ("id", "product_quantity", "discount_type", "value")
