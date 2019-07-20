
from drfaddons import generics

from manager.permissions import IsStaff


class IndentView(generics.OwnerListCreateAPIView):

    from .models import Indent
    from .serializers import IndentSerializer
    permission_classes = (IsStaff, )
    queryset = Indent.objects.all()
    serializer_class = IndentSerializer


class IndentRequestView(generics.OwnerListCreateAPIView):

    from .models import IndentRequest
    from .serializers import IndentRequestSerializer
    permission_classes = (IsStaff,)
    queryset = IndentRequest.objects.all()
    serializer_class = IndentRequestSerializer


class IndentRequestDetailView(generics.OwnerListCreateAPIView):

    from .models import IndentRequestDetail
    from .serializers import IndentRequestDetailSerializer
    permission_classes = (IsStaff,)
    queryset = IndentRequestDetail.objects.all()
    serializer_class = IndentRequestDetailSerializer


class BoxView(generics.OwnerListCreateAPIView):

    from .models import Box
    from .serializers import BoxSerializer
    permission_classes = (IsStaff,)
    queryset = Box.objects.all()
    serializer_class = BoxSerializer


class BoxItemView(generics.OwnerListCreateAPIView):

    from .models import BoxItem
    from .serializers import BoxItemSerializer
    permission_classes = (IsStaff,)
    queryset = BoxItem.objects.all()
    serializer_class = BoxItemSerializer

