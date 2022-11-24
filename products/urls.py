from django.urls import include, path
# import routers
from rest_framework.routers import DefaultRouter

# from .api import (BrandDetailApi, BrandListApi, CategoryDetailApi,
#                   CategoryListApi, ProductDetailApi, ProductListApi,
#                   )
from .api import BrandViewSet, CategoryViewSet, ProductViewSet
from .views import (BrandDetail, BrandList, CategoryList, ProductDetail,
                    ProductList)

app_name = 'products'

router = DefaultRouter()
router.register('myproducts', ProductViewSet, basename='products')
router.register('mybrands', BrandViewSet, basename='brands')
router.register('mycategories', CategoryViewSet, basename='categories')







urlpatterns = [
     path('', ProductList.as_view(), name='product_list'),
     path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
     path('brands/', BrandList.as_view(), name='brand_list'),
     path('brands/<int:pk>/', BrandDetail.as_view(), name='brand_detail'),
     path('categories/', CategoryList.as_view(), name='category_list'),
     # ---------------------------------------------------------------------
     # path('api/list/', product_list_api, name='product_list_api'),
     # path('api/list/<int:pk>/', product_detail_api, name='product_detail_api'),
     # ---------------------------------------------------------------------
     #     path('list/api/', ProductListApi.as_view(), name='product_list_api'),
     #     path('list/api/<int:pk>/',
     #          ProductDetailApi.as_view(),
     #          name='product_detail_api'),
     #     path('brands/api/', BrandListApi.as_view(), name='brand_list_api'),
     #     path('brands/api/<int:pk>/',
     #          BrandDetailApi.as_view(),
     #          name='brand_detail_api'),
     #     path('categories/api/',
     #          CategoryListApi.as_view(),
     #          name='category_list_api'),
     #     path('categories/api/<int:pk>/',
     #          CategoryDetailApi.as_view(),
     #          name='category_detail_api'),
     # ---------------------------------------------------------------------
     path('api/', include(router.urls)),
]
