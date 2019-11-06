from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsManager
from .filters import IsManagerFilterBackend
from .models import OutletProduct, OutletSubProduct
from .serializers import OutletProductSerializer, ManageSubProductSerializer


class OutletView(generics.ListAPIView):
    from .models import Outlet
    from .serializers import OutletSerializer

    permission_classes = (IsManager,)
    filter_backends = (DjangoFilterBackend, IsManagerFilterBackend)
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer


class OutletProductView(generics.ListAPIView):

    permission_classes = (IsManager,)
    queryset = OutletProduct.objects.all()
    filter_backends = (DjangoFilterBackend, IsManagerFilterBackend)
    serializer_class = OutletProductSerializer


class ManageStockAPIView(generics.RetrieveUpdateAPIView):
    queryset = OutletSubProduct.objects.all()
    filter_backends = (DjangoFilterBackend, IsManagerFilterBackend)
    serializer_class = ManageSubProductSerializer
