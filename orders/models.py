from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from shop.models import Product
# Create your models here.

class Order(models.Model):
    SEND_CHOICES = (
        ('p','on proccess'),
        ('s','sent'),
        ('o','out of Storage'),
        ('w','Waiting')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='uorder')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=1,choices=SEND_CHOICES,default='w')

    class Meta:
        ordering = ['is_paid','status','-created']

    def __str__(self):
        return str(self.user)

    def total_price(self):
        return sum(item.get_cost() for item in self.item.all())

    def get_absolute_url(self):
        return reverse('dashboard:order')


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='item')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_item')
    price = models.IntegerField()
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return str(self.pk)

    def get_cost(self):
        return self.price*self.quantity