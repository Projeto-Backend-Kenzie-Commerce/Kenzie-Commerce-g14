from django.db import models


class ShopCart(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="shop_cart",
    )

    product = models.ManyToManyField("products.Product", related_name="products")
