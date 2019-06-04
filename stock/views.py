from django.shortcuts import render
from drfaddons import generics


class StockView(generics.OwnerListCreateAPIView):
    from .models import Stock
    from .serializers import StockSerializer

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
