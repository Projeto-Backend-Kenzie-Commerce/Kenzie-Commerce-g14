from django.db import models


class ShopCart(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="shop_cart",
    )

    products = models.ManyToManyField("products.Product", related_name="shop_cart")


class CartProduct(models.Model):
    cart = models.ForeignKey(
        ShopCart, on_delete=models.CASCADE, related_name="cart_product"
    )
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
