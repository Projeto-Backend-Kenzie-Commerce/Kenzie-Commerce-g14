from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField()
    stock_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(null=True, default=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="products",
    )