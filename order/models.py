
from django.db import models
from account.models import Customer
from product.models import Product

class Order(models.Model):
    STATUSES = [
        ('PENDING', 'pending'),
        ('INPROGRESS', 'inprogress'),
        ('COMPLATED', 'complated'),
        ('CANCELED', 'canceled'),

    ]
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    required_date = models.DateTimeField(null=True, blank=True)
    shipped_date = models.DateTimeField(null=True,blank=True)
    canceled_date = models.DateTimeField(null=True,blank=True)
    status = models.CharField(max_length=10, choices=STATUSES, default='PENDING')

class Order_detail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True, related_name='orders')
    quantity = models.IntegerField(default=1)
