from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Order

        model = Order
        fields = ('id', 'name', 'mobile', 'email', 'discount', 'outlet')


class SubOrderSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import SubOrder

        model = SubOrder
        fields = ('order', 'product', 'price', 'quantity', 'total')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Transaction

        model = Transaction
        fields = ('order', 'amount', 'mode')
