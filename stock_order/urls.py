from django.urls import path
from . import views

app_name = "stock_order"

urlpatterns = [
    path('', views.IndentView.as_view(), name="Indent"),
    path('indentRequest/', views.IndentRequestView.as_view(), name="Indent "
                                                                   "Request"),
    path('indentRequest/indentRequestDetails/',
         views.IndentRequestDetailView.as_view(),
         name="Indent Request Details"),
    path('box/', views.BoxView.as_view(), name="Box"),
    path('box/boxItem/', views.BoxItemView.as_view(), name="Box Items")
]
