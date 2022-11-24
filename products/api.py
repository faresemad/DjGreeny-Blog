from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .models import Brand, Category, Product
from .serializers import (BrandDetailSerializer, BrandSerializer,
                          CategoryDetailSerializer, CategorySerializer,
                          ProductSerializer)

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


# class ProductListApi(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['name', 'price']
#     permission_classes = [IsAuthenticated]


# class ProductDetailApi(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]


# class BrandListApi(generics.ListAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['name']
#     permission_classes = [IsAuthenticated]

# class BrandDetailApi(generics.RetrieveAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandDetailSerializer
#     permission_classes = [IsAuthenticated]


# class CategoryListApi(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['name']
#     permission_classes = [IsAuthenticated]

# class CategoryDetailApi(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryDetailSerializer
#     permission_classes = [IsAuthenticated]


######### ViewSets #########

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'price']
    # permission_classes = [IsAuthenticated]

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    # permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    # permission_classes = [IsAuthenticated]