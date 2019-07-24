from drfaddons import generics
from rest_framework.response import Response
from manager.permissions import IsStaff


class OrderView(generics.OwnerCreateAPIView):
    from .models import Order
    from .serializers import OrderSerializer
    permission_classes = (IsStaff,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SubOrderView(generics.OwnerCreateAPIView):
    permission_classes = (IsStaff,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        from order.models import SubOrder
        from outlet.models import OutletSubProduct
        from order.models import Order
        order = Order.objects.get(pk=request.data["order"])
        outletproduct = OutletSubProduct.objects.get(pk=request.data["product"])

        if order and outletproduct and self.request.user:
            suborder = SubOrder.objects.create(created_by=self.request.user, order=order, product=outletproduct,
                                               price=request.data["price"], quantity=request.data["quantity"],)
            suborder.save()
            outletproduct.display_stock = int(outletproduct.display_stock) - int(request.data["quantity"])
            outletproduct.save()
            return Response({"Success": "True"})
        else:
            return Response({"Failure": "False"})


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
