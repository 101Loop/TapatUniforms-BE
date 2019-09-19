from rest_framework import generics

from manager.permissions import IsStaff


class OutletView(generics.ListAPIView):
    from .models import Outlet
    from .serializers import OutletSerializer

    permission_classes = (IsStaff,)
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer


class OutletProductView(generics.ListAPIView):
    from .models import OutletProduct
    from .serializers import OutletProductSerializer

    permission_classes = (IsStaff,)
    queryset = OutletProduct.objects.all()
    serializer_class = OutletProductSerializer
