from rest_framework import generics

from manager.permissions import IsManager


class OutletView(generics.ListAPIView):
    from .models import Outlet
    from .serializers import OutletSerializer

    permission_classes = (IsManager,)
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer


class OutletProductView(generics.ListAPIView):
    from .models import OutletProduct
    from .serializers import OutletProductSerializer

    permission_classes = (IsManager,)
    queryset = OutletProduct.objects.all()
    serializer_class = OutletProductSerializer
