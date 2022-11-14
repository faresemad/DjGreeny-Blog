from django.contrib.auth.models import User
from django.db import models

from products.models import Product
from utils.generateCode import generate_code

# Create your models here.
ORDER_STATUS = (("recieved", "Recieved"), ("processing", "Processing"),
                ("shipped", "Shipped"), ("delivered", "Delivered"))


class Orders(models.Model):
    status = models.CharField(max_length=20,
                              choices=ORDER_STATUS,
                              default="recieved")
    user = models.ForeignKey(User,
                             related_name='user_order',
                             on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True, default=generate_code)
    orderTime = models.DateTimeField(auto_now_add=True)
    deliveryTime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.code


class OrderDetail(models.Model):
    order = models.ForeignKey(Orders,
                              related_name='order_detail',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='product_order',
                                on_delete=models.SET_NULL,
                                null=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.order)


CART_STATUS = (("Inprogress", "Inprogress"), ("Completed", "Completed"))


class Cart(models.Model):
    status = models.CharField(max_length=20,
                              choices=CART_STATUS,
                              default="recieved")
    user = models.ForeignKey(User,
                             related_name='user_cart',
                             on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True, default=generate_code)

    def __str__(self):
        return self.code

    # get total price of cart
    def get_total(self):
        total = 0
        for item in self.cart_detail.all():
            total += item.get_total()
        return total


class CartDetail(models.Model):
    order = models.ForeignKey(Cart,
                              related_name='cart_detail',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='product_cart',
                                on_delete=models.SET_NULL,
                                null=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    total = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.order)