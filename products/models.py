from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.DecimalField(decimal_places=2)
    description = models.TextField()
    stock_quantity = models.IntegerField()
    # user = 