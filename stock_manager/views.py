from django.shortcuts import render
from rest_framework.generics import views
from rest_framework.permissions import AllowAny
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
            if outlet_sub_product.warehouse_stock > int(request.data["item_count"]):
                outlet_sub_product.warehouse_stock = outlet_sub_product.warehouse_stock - int(request.data["item_count"])
                outlet_sub_product.display_stock = outlet_sub_product.display_stock + int(request.data["item_count"])
                outlet_sub_product.save()

                box_item = BoxItem.objects.all()
                x = int(0)
                item_left = int(request.data["item_count"])
                print(box_item[0].num_of_item)
                while item_left is not 0:
                    print("here")
                    if box_item[x].num_of_item >= item_left:
                        print("here also")
                        box_item[x].num_of_item = box_item[x].num_of_item - item_left
                        item_left = 0
                        box_item[x].save()
                    else:
                        item_left = item_left - box_item[x].num_of_item
                        box_item[x].num_of_item = 0
                        box_item[x].save()
                        x = x+1
                return Response({"success": "true"})
            else:
                return Response({"Failure": "Shortage"})
        else:
            return Response({"Failure": "Product Not Found"})
