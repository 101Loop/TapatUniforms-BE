from django.urls import path
from . import views

app_name = 'urls'

urlpatterns = [
    path('', views.StockView.as_view(), name='list-stocks'),
]
