from django.db import models
from decimal import Decimal
from django.utils import timezone
from adminLoginApp.models import Product

class Order(models.Model):
   customer_name = models.CharField(max_length = 200)
   order_date = models.DateField(default=timezone.now)

   def __str__(self):
    return f"Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def save(self, *args, **kwargs):
        self.subtotal = self.product.price * self.quantity
        super(OrderItem, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.product.name} - {self.quantity} x ${self.product.price} = ${self.subtotal}"
    
    
   