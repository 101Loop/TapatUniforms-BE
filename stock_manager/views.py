from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from manager.permissions import IsStaff


class StockTransferView(UpdateAPIView):
    from .serializers import StockManagerSerializer
    permission_classes = (IsStaff, )
    serializer_class = StockManagerSerializer

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # for receiving data from serializer
        serializer.is_valid(raise_exception=True)
        from outlet.models import OutletProduct
        from outlet.models import OutletSubProduct
        from stock_order.models import BoxItem
        from stock_order.models import Box
        box = Box.objects.get(box_code=serializer.validated_data["box_code"])
        outlet_products = OutletProduct.objects.get(
            pk=serializer.validated_data['outlet_product'],
            outlet=serializer.validated_data['outlet']
        )
        outlet_sub_product = OutletSubProduct.objects.get(
            outlet_product=outlet_products,
            pk=serializer.validated_data['outlet_sub_product']
        )
        box_item = BoxItem.objects.get(box=box, product=outlet_sub_product)
        if outlet_sub_product:

            if box_item.item_scanned >= serializer.validated_data["item_count"]:
                outlet_sub_product.warehouse_stock = \
                    outlet_sub_product.warehouse_stock - serializer.validated_data["item_count"]
                outlet_sub_product.display_stock = \
                    outlet_sub_product.display_stock + serializer.validated_data["item_count"]
                outlet_sub_product.save()
                item_left = serializer.validated_data["item_count"]

                if box_item.product == outlet_sub_product:
                    if box_item.item_scanned >= item_left:
                        box_item.item_scanned = box_item.item_scanned - item_left
                        box_item.item_in_shelf = box_item.item_in_shelf + item_left
                        box_item.save()

                return Response({"success": "true"})
            else:
                return Response({"Failure": "Shortage"})
        else:
            return Response({"Failure": "Product Not Found"})
