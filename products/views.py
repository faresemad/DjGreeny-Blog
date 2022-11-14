from django.db.models.aggregates import Count
from django.shortcuts import render
from django.views.generic import DetailView, ListView

# Create your views here.
from .models import Brand, Category, Product


class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 25


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
        context['brand_list'] = Brand.objects.all().annotate(
            ProductCount=Count('product_brand'))
        return context


class BrandDetail(DetailView):
    model = Brand
    template_name = 'products/brand_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand_products"] = Product.objects.filter(brand=self.object)
        return context


class CategoryList(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'