from django.test import TestCase
from rest_framework.test import APIClient
from .models import Outlet
from .models import OutletProduct
from product.models import Product, CategoryMaster
from drf_user.models import User


class OutletProductTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username="NiKlaus", email="lsoit@gmail.com", mobile="70156s3438"
        )
        cls.category = CategoryMaster.objects.create(
            name="Shirt", image="image.jpg", created_by=cls.user
        )
        cls.product = Product.objects.create(
            name="shirt 1",
            created_by=cls.user,
            category=cls.category,
            sku="ss",
            product_type="HS",
        )
        cls.outlet = Outlet.objects.create(
            name="Outlet Shop",
            created_by=cls.user,
            location="kurukshetra",
            short_name="out",
        )
        cls.outProduct = OutletProduct.objects.create(
            created_by=cls.user,
            outlet=cls.outlet,
            product=cls.product,
            price="1233",
            image="image.jpg",
            color="Red",
            color_code="#fff",
            size="24",
            warehouse_stock=12,
            display_stock=12,
        )

    def test_api(self):
        client = APIClient()
        response = client.get("/api/outlets/products/")
        assert response.status_code == 200
