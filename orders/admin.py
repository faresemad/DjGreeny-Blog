from django.contrib import admin

from .models import Cart, CartDetail, OrderDetail, Orders

# Register your models here.
admin.site.register(Orders)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(CartDetail)