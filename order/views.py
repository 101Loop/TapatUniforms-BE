from drfaddons import generics

from manager.permissions import IsManager
from .models import SubOrder
from django.http import HttpResponse
from TapatUniforms.utils import render_to_pdf


class OrderView(generics.OwnerCreateAPIView):
    from .models import Order
    from .serializers import OrderSerializer

    permission_classes = (IsManager,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SubOrderView(generics.OwnerCreateAPIView):

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


def invoice(self, request, *args, **kwargs):
    instance: SubOrder = self.get_object()
    data = {
        "order_id": str(instance.order_id),
        "order_date": str(instance.order.create_date.date().strftime("%d %b %Y")),
        "name": str(instance.order.name),
        "email": str(instance.order.email),
        "mobile": str(instance.order.email),
        "product": str(instance.product.name),
        "price": str(instance.price),
        "qty": str(instance.quantity),
        "total": str(instance.order.total),
    }
    pdf = render_to_pdf("order/invoice.html", data)
    return HttpResponse(pdf, content_type="application/pdf")
