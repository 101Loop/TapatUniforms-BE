from django.test import TestCase
from drf_user.models import User
from rest_framework.test import APIClient

from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CategoryMaster, Product
from product import views

# class Testing(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = User.objects.create(
#             username="NiKlaus", email="lsoit@gmail.com", mobile="70156s3438"
#         )
#         cls.category = CategoryMaster.objects.create(
#             name="Shirt", image="image.jpg", created_by=cls.user
#         )
#         cls.product = Product.objects.create(
#             name="shirstko",
#             created_by=cls.user,
#             category=cls.category,
#             sku="ss",
#             product_type="HS",
#         )
#
#     def test_api(self):
#         client = APIClient()
#         response = client.get("/api/categories/products/")
#         assert response.status_code == 200


class ProductCategoryTest(APITestCase):
    """ To test the Product category API """

    def test_get_product_category(self):
        pass
