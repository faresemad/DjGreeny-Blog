from django.shortcuts import render
from django.views.generic import DetailView, ListView

# Create your views here.
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'