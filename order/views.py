from drfaddons import generics


class OrderView(generics.OwnerCreateAPIView):
    from .models import Order
    from .serializers import OrderSerializer

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SubOrderView(generics.OwnerCreateAPIView):
    from .models import SubOrder
    from .serializers import SubOrderSerializer

    queryset = SubOrder.objects.all()
    serializer_class = SubOrderSerializer


class TransactionView(generics.OwnerCreateAPIView):
    from order.models import Transaction
    from order.serializers import TransactionSerializer

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
