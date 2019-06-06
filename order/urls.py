from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.OrderView.as_view(), name='list-create-products'),
    path('suborder/', views.SubOrderView.as_view(),
         name='list-create-suborder'),
    path('transaction/', views.TransactionView.as_view(),
         name='list-create-transaction')
]
