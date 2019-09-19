from django.urls import path
from . import views

app_name = "outlet"

urlpatterns = [
    path("", views.OutletView.as_view(), name="list-outlet"),
    path("products/", views.OutletProductView.as_view(), name="list-outlet-product"),
]
