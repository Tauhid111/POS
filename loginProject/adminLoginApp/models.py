from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
        
class Permission(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField (Permission)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=255)
    #category = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name



class Tax(models.Model):
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    sd = models.DecimalField(max_digits=10, decimal_places=2)


class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

