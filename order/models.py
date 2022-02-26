
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
    def __str__(self):
        return f'{self.customer.get_name} - order: {self.id}'
    def items_count(self):
        return self.details.count()
    def total_price(self):
        return sum([ i.product.price * i.quantity for i in self.details.all() ])

class Order_detail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True, related_name='orders')
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f'order:{self.order.id} - product:{self.product} - quantity: {self.quantity}'
    def total_price(self):
        return self.product.price * self.quantity
