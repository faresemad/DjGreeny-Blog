from django.contrib import admin

from .models import Brand, Category, Product, ProductImage, ProductReview


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(Brand)
admin.site.register(Category)