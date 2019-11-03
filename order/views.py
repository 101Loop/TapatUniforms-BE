from drfaddons import generics

from manager.permissions import IsManager


class OrderView(generics.OwnerCreateAPIView):
    from .models import Order
    from .serializers import OrderSerializer

    permission_classes = (IsManager,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SubOrderView(generics.OwnerCreateAPIView):
    from .models import SubOrder
    from .serializers import SubOrderSerializer

    permission_classes = (IsManager,)
    queryset = SubOrder.objects.all()
    serializer_class = SubOrderSerializer


class TransactionView(generics.OwnerCreateAPIView):
    from order.models import Transaction
    from order.serializers import TransactionSerializer

    permission_classes = (IsManager,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class DiscountView(generics.OwnerListAPIView):
    from order.models import Discount
    from order.serializers import DiscountSerializer

    permission_classes = (IsManager,)
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
