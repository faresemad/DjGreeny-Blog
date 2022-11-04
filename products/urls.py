from django.urls import path

from .views import ProductDetail, ProductList

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]
