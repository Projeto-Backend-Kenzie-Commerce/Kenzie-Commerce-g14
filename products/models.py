from django.db import models


class Product(models.Model):
    # class Meta:
    #     ordering = ["id"]

    name = models.CharField(max_length=80)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField()
    stock_quantity = models.IntegerField()
    category = models.CharField(max_length=80)
    is_available = models.BooleanField(null=True, default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="products",
    )


# RATING_CHOICES = (
#     (1, "1 estrela"),
#     (2, "2 estrelas"),
#     (3, "3 estrelas"),
#     (4, "4 estrelas"),
#     (5, "5 estrelas"),
# )


# class CustomerReview(models.Model):
#     rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
#     comment = models.TextField(null=True, blank=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     user = models.ForeignKey(
#         "users.User", on_delete=models.CASCADE, related_name="customer_review"
#     )
#     product = models.ForeignKey(
#         "products.Product", on_delete=models.CASCADE, related_name="customer_review"
#     )
