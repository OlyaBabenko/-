from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    imgUrl = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    oldPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    actualPrice = models.DecimalField(max_digits=10, decimal_places=2)
    objects = models.Manager()


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product.name}, {self.quantity}'


class Order(models.Model):
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(OrderItem)
