from rest_framework.generics import views
from rest_framework.response import Response
from manager.permissions import IsStaff


class StockTransferView(views.APIView):

    permission_classes = (IsStaff, )

    def post(self, request):
        from outlet.models import OutletProduct
        from outlet.models import OutletSubProduct
        from stock_order.models import BoxItem
        outlet_products = OutletProduct.objects.get(
            name=request.data['name'],
            outlet=request.data['outlet']
        )
        outlet_sub_product = OutletSubProduct.objects.get(
            outlet_product=outlet_products,
            size=request.data['size']
        )
        if outlet_sub_product:
            if outlet_sub_product.warehouse_stock >= int(request.data["item_count"]):
                outlet_sub_product.warehouse_stock = outlet_sub_product.warehouse_stock - int(request.data["item_count"])
                outlet_sub_product.display_stock = outlet_sub_product.display_stock + int(request.data["item_count"])
                outlet_sub_product.save()
                item_left = int(request.data["item_count"])
                for box_item in BoxItem.objects.all():
                    if box_item.product == outlet_sub_product:
                        if box_item.num_of_item >= item_left:
                            box_item.num_of_item = box_item.num_of_item - item_left
                            box_item.save()
                            break
                        else:
                            item_left = item_left - box_item.num_of_item
                            box_item.num_of_item = 0
                            box_item.save()
                return Response({"success": "true"})
            else:
                return Response({"Failure": "Shortage"})
        else:
            return Response({"Failure": "Product Not Found"})
