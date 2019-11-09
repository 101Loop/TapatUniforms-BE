from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django_xhtml2pdf.utils import generate_pdf
from drfaddons import generics
from rest_framework.generics import ListCreateAPIView
from manager.permissions import IsManager
from .models import SubOrder, Order


class OrderView(generics.OwnerCreateAPIView):
    from .models import Order
    from .serializers import OrderSerializer

    permission_classes = (IsManager,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class AllOrderView(generics.OwnerListAPIView):
    from .models import Order
    from .serializers import AllOrderSerializer

    queryset = Order.objects.all()
    serializer_class = AllOrderSerializer


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


class DiscountView(ListCreateAPIView):
    from order.models import Discount
    from order.serializers import DiscountSerializer

    permission_classes = (IsManager,)
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

    def perform_create(self, serializer):
        serializer.save(created_by_id=self.request.user.id)


class PdfResponseMixin(object):
    pdf_name = "invoice"

    def get_pdf_name(self):
        return self.pdf_name

    def render_to_response(self, context, **response_kwargs):
        context = self.get_context_data()
        template = self.get_template_names()[0]
        resp = HttpResponse(content_type="application/pdf")
        resp["Content-Disposition"] = 'attachment; filename="{0}.pdf"'.format(
            self.get_pdf_name()
        )
        result = generate_pdf(template, file_object=resp, context=context)
        return result


class OrderPdfDetailView(PdfResponseMixin, DetailView):
    template_name = "order/example.html"
    context_object_name = "order"
    model = Order
