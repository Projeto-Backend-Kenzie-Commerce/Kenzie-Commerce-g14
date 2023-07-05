from django.db import models


class ShopCart(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="shop_cart",
    )

    products = models.ManyToManyField("products.Product", through="CartProduct")

    def get_subtotal(self):
        return sum(cart_product.total for cart_product in self.cartproduct_set.all())


class CartProduct(models.Model):
    cart = models.ForeignKey(ShopCart, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total = models.DecimalField(decimal_places=2, max_digits=5)

    def save(self, *args, **kwargs):
        self.total = self.product.price * self.quantity
