from rest_framework import generics
from rest_framework.permissions import AllowAny


class OutletView(generics.ListAPIView):
    from .models import Outlet
    from .serializers import OutletSerializer

    permission_classes = (AllowAny, )
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer


class OutletProductView(generics.ListAPIView):
    from .models import OutletProduct
    from .serializers import OutletProductSerializer

    permission_classes = (AllowAny,)
    queryset = OutletProduct.objects.all()
    serializer_class = OutletProductSerializer
