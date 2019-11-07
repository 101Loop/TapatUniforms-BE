from drfaddons import generics
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from manager.permissions import IsManager
from .filters import IsManagerFilterBackend


class IndentRequestView(generics.OwnerCreateAPIView):
    """
    This will Raise Indent Request for the Warehouse
    """

    from .models import IndentRequest
    from .serializers import IndentRequestSerializer

    permission_classes = (IsManager,)
    queryset = IndentRequest.objects.all()
    # filter_backends = (DjangoFilterBackend, IsManagerFilterBackend)
    serializer_class = IndentRequestSerializer


# ToDo: Add Permission so that only indents linked to a school is retrieved for
#  a user linked to the same school
class IndentView(ListAPIView):
    """
    This will list all the Shipped indents for a school
    """

    from .models import Indent
    from .serializers import IndentSerializer

    permission_classes = (IsManager,)
    queryset = Indent.objects.all()
    filter_backends = (DjangoFilterBackend, IsManagerFilterBackend)
    serializer_class = IndentSerializer


# ToDo: box linked to a school should be retrieved only by those user that
#  are linked to the same school
class BoxView(ListAPIView):
    """
    This will list all the boxes available inside the indent
    """

    from .models import Box
    from .serializers import BoxSerializer

    permission_classes = (IsManager,)
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().filter(indent=self.kwargs["indent"])
        return super().get(request, *args, **kwargs)


# ToDo: box Items linked to a school should be retrieved only by those user
#  that are linked to the same school
class BoxItemView(ListAPIView):
    """
    This will list all the items available inside the box
    """

    from .models import BoxItem
    from .serializers import BoxItemSerializer

    permission_classes = (IsManager,)
    queryset = BoxItem.objects.all()
    serializer_class = BoxItemSerializer
    filter_backends = (DjangoFilterBackend, IsManagerFilterBackend)

    def get(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().filter(box=self.kwargs["box"])
        return super().get(request, *args, **kwargs)


class BoxItemUpdateView(RetrieveUpdateAPIView):
    """
    This will update the items available inside the box
    """

    from .models import BoxItem
    from .serializers import BoxItemSerializer

    permission_classes = (IsManager,)
    queryset = BoxItem.objects.all()
    serializer_class = BoxItemSerializer
    filter_backends = (DjangoFilterBackend, IsManagerFilterBackend)
