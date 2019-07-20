from drfaddons import generics

from manager.permissions import IsStaff


class OrderView(generics.OwnerCreateAPIView):
    from .models import Order
    from .serializers import OrderSerializer
    permission_classes = (IsStaff,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SubOrderView(generics.OwnerCreateAPIView):
    from .models import SubOrder
    from .serializers import SubOrderSerializer
    permission_classes = (IsStaff,)
    queryset = SubOrder.objects.all()
    serializer_class = SubOrderSerializer


class TransactionView(generics.OwnerCreateAPIView):
    from order.models import Transaction
    from order.serializers import TransactionSerializer
    permission_classes = (IsStaff,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class DiscountView(generics.OwnerListAPIView):
    from order.models import Discount
    from order.serializers import DiscountSerializer
    permission_classes = (IsStaff,)
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
