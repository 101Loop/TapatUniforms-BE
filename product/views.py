from rest_framework import generics
from rest_framework.permissions import AllowAny


class ProductView(generics.ListAPIView):
    from .models import Product
    from .serializers import ProductSerializer

    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryView(generics.ListAPIView):
    from .models import CategoryMaster
    from .serializers import CategorySerializer

    permission_classes = (AllowAny,)
    queryset = CategoryMaster.objects.all()
    serializer_class = CategorySerializer
