"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from capstore.views import *
from capstore import views
from profileapp import views as user_views
from . import swagger



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/brand/', views.BrandAPIViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('api/v1/brand/<int:pk>/', views.BrandAPIViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('api/v1/product/', views.product_list_view),
    path('api/v1/product/<int:id>/', views.product_item_view),
    path('api/v1/bestseller/', views.bestseller_view),
    path('api/v1/favorite/', views.favorite_view),
    path('api/v1/sale/', views.sale_view),
    path('api/v1/order/', views.order_view),
    path('api/v1/orderitem/', views.orderitem_view),
    path('api/v1/authorization/', user_views.AuthorizationAPIView.as_view()),
    path('api/v1/registration/', user_views.RegistrationAPIView.as_view()),
]

# urlpatterns += swagger.urlpatterns