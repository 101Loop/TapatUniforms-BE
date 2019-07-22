from rest_framework.generics import views
from rest_framework.response import Response
from manager.permissions import IsStaff


class StockTransferView(views.APIView):

    permission_classes = (IsStaff, )

