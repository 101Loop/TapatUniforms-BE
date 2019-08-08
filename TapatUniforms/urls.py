"""TapatUniforms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Tapat Uniform API",
        default_version='v1',
        description="API definition for Tapat Uniform",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('api/user/',
                       include('drf_user.urls', namespace='user')),
                  path('api/order/', include('order.urls', namespace='order')),
                  path('api/outlets/',
                       include('outlet.urls', namespace='outlet')),
                  path('api/categories/',
                       include('product.urls', namespace='product')),
                  path('api/school/',
                       include('school.urls', namespace='school')),
                  path('api/stockOrder/',
                       include('stock_order.urls', namespace='Stock '
                                                             'Order')),

                  re_path(r'^swagger(?P<format>\.json|\.yaml)$',
                          schema_view.without_ui(cache_timeout=0),
                          name='schema-json'),
                  path('swagger/',
                       schema_view.with_ui('swagger', cache_timeout=0),
                       name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
                       name='schema-redoc'),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
