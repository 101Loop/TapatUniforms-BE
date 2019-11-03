from rest_framework import generics
from rest_framework.permissions import AllowAny

from manager.permissions import IsManager


class ProductView(generics.ListAPIView):
    from .models import Product
    from .serializers import ProductSerializer

    permission_classes = (IsManager,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryView(generics.ListAPIView):
    from .models import CategoryMaster
    from .serializers import CategorySerializer

    permission_classes = (IsManager,)
    queryset = CategoryMaster.objects.all()
    serializer_class = CategorySerializer
