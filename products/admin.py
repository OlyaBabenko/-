from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'name', 'imgUrl', 'weight', 'description', 'oldPrice', 'actualPrice')


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "address", "phone")
