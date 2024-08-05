import csv
from decimal import Decimal
from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def in_db_from_csv(self):
        with open('products_restaurant.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                restaurant = Restaurant(
                    id=int(row["id"]),
                    name=row["name"]
                )
                restaurant.save()
        with open('products_product.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                instance = Restaurant.objects.get(id=int(row['restaurant_id']))
                if row["oldPrice"] == '':
                    row["oldPrice"] = None
                else:
                    row["oldPrice"] = Decimal(row["oldPrice"])
                product = Product(
                    id=int(row['id']),
                    name=row['name'],
                    imgUrl=row["imgUrl"],
                    weight=row["weight"],
                    description=row["description"],
                    oldPrice=row["oldPrice"],
                    actualPrice=Decimal(row["actualPrice"]),
                    restaurant=instance
                )
                product.save()


class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    imgUrl = models.ImageField(upload_to="product_pictures/", blank=True, null=True)
    # imgUrl = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    oldPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    actualPrice = models.DecimalField(max_digits=10, decimal_places=2)
    objects = ProductManager()


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product.name}, {self.quantity}'


class Recipient(models.Model):
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        if self.user.username:
            return self.user.username
        return "Anonymous"


class Order(models.Model):
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
