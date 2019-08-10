from django.urls import path
from . import views

app_name = "stock_order"

urlpatterns = [
    path('indent/', views.IndentView.as_view(), name="Indent"),
    path('indentRequest/', views.IndentRequestView.as_view(),
         name="Indent Request"),
    path('indent/<int:pk>/boxes/', views.BoxView.as_view(), name="Box"),
    path('box/<int:box>/items/', views.BoxItemView.as_view(), name="Box Items")
]
