from django.db import models
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel


class StatusChoices(models.TextChoices):
    CONFIRMED = "confirmed"
    IN_PROGRESS = "in_progress"
    DELIVERED = "delivered"
    CANCELED = "canceled"


class Order(SafeDeleteModel):
    status = models.CharField(
        max_length=25, choices=StatusChoices.choices, default=StatusChoices.CONFIRMED
    )
    product_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )
    is_employee = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders_sellers"
    )
    product = models.ManyToManyField("products.Product", related_name="orders")
    _safedelete_policy = SOFT_DELETE
