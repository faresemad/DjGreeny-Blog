from rest_framework import serializers

from .models import Brand, Category, Product


class BrandSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Brand
        fields = ['name', 'image', 'category']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'image']


class ProductSerializer(serializers.ModelSerializer):
    # brand = serializers.StringRelatedField()
    # category = serializers.StringRelatedField()
    brand = BrandSerializer()
    category = CategorySerializer()
    price_with_discount = serializers.SerializerMethodField()

    def get_price_with_discount(self, product):
        return int(product.price) - int(product.price) * .15
        # return (product.price - (product.price * product.discount / 100))

    class Meta:
        model = Product
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    products = ProductSerializer(source='product_brand', many=True)

    class Meta:
        model = Brand
        fields = ['name', 'image', 'category','products']


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='product_category', many=True)

    class Meta:
        model = Category
        fields = ['name', 'image', 'products']
