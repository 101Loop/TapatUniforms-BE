from django.urls import path

from . import views

app_name = "product"

urlpatterns = [
    path("", views.CategoryView.as_view(), name="list-category"),
    path("products/", views.ProductView.as_view(), name="list=product"),
]
