from django.urls import path
from . import views

app_name = "stock_manager"

urlpatterns = [
    path('', views.StockTransferView.as_view(), name="Update Stock Transfer")
]
