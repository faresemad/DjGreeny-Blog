from django.shortcuts import render
from django.views.generic import DetailView, ListView

# Create your views here.
from .models import Brand, Category, Product


class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

class BrandList(ListView):
    model = Brand
    template_name = 'products/brand_list.html'
    context_object_name = 'brands'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

class BrandDetail(DetailView):
    model = Brand
    template_name = 'products/brand_detail.html'
