from django.db import models
from django.contrib.auth.models import User


class StoreCategory(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='store_category_pictures/')


class ItemCategory(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='item_category_pictures/')


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customer_avatars/', blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)


class StoreOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='store_owner_avatars/', blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)


class Store(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='item_pictures/')
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    info = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class MyBag(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
