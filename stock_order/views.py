
from drfaddons import generics


class IndentView(generics.OwnerListCreateAPIView):

    from .models import Indent
    from .serializers import IndentSerializer
    queryset = Indent.objects.all()
    serializer_class = IndentSerializer


class IndentRequestView(generics.OwnerListCreateAPIView):

    from .models import IndentRequest
    from .serializers import IndentRequestSerializer

    queryset = IndentRequest.objects.all()
    serializer_class = IndentRequestSerializer


class IndentRequestDetailView(generics.OwnerListCreateAPIView):

    from .models import IndentRequestDetail
    from .serializers import IndentRequestDetailSerializer

    queryset = IndentRequestDetail.objects.all()
    serializer_class = IndentRequestDetailSerializer


class BoxView(generics.OwnerListCreateAPIView):

    from .models import Box
    from .serializers import BoxSerializer

    queryset = Box.objects.all()
    serializer_class = BoxSerializer


class BoxItemView(generics.OwnerListCreateAPIView):

    from .models import BoxItem
    from .serializers import BoxItemSerializer

    queryset = BoxItem.objects.all()
    serializer_class = BoxItemSerializer

