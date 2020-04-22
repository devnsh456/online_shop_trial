from django.db import models
from product.model import Product
# Create your models here.

class Order_cus(models.Model):
    first_name=models.CharField(max_length=125)
    last_name=models.CharField(max_length=125)
    mob_num=models.BigIntegerField()
    street=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering:('-created',)


class OrderItem(models.Model):
    order=Models.ForeignKey(Order,on_delete=Models.CASCADE,related_name='items')

    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price * self.quantity
