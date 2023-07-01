from django.db import models


class StatusChoices(models.TextChoices):
    CONFIRMED = "confirmed"
    IN_PROGRESS = "in_progress"
    DELIVERED = "delivered"


class Order(models.Model):
    status = models.CharField(
        max_length=25, choices=StatusChoices.choices, default=StatusChoices.CONFIRMED
    )
    product_quantity = models.IntegerField()
    created_at = models.DateTimeField()

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="orders_owner")
    is_employee = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="orders_sellers")
    product = models.ManyToManyField("users.User", related_name="orders")
