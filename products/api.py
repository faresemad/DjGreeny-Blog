from rest_framework import generics

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def product_detail_api(request, pk):
#     product = Product.objects.get(pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)


class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandListApi(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryListApi(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer