from django.db      import models

from user.models    import User
from product.models import ProductSize

class ExpirationType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'expiration_types'

class Ask(models.Model):
    user            = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product_size    = models.ForeignKey('product.ProductSize', on_delete=models.CASCADE)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField()
    order_status    = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)
    matched_at      = models.DateTimeField(null=True)
    total_price     = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    order_number    = models.CharField(null=True, max_length=100)
    

    class Meta:
        db_table = 'asks'

class Bid(models.Model):
    user            = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product_size    = models.ForeignKey('product.ProductSize', on_delete=models.CASCADE)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField()
    order_status    = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)
    matched_at      = models.DateTimeField(null=True)
    total_price     = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    order_number    = models.CharField(null=True, max_length=100)

    class Meta:
        db_table = 'bids'

class OrderStatus(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'order_status'

class OrderType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'order_types'

class Order(models.Model):
    ask          = models.ForeignKey('Ask', on_delete=models.CASCADE, null=True)
    bid          = models.ForeignKey('Bid', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'orders'