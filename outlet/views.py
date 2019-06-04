from django.shortcuts import render
from drfaddons import generics


class OutletView(generics.GenericAPIView):
    from .models import Outlet
    from .serializers import OutletSerializer

    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
