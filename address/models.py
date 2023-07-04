from django.db import models
from users.models import User


class Address(models.Model):
    class Meta:
        ordering = ["id"]

    street = models.CharField(max_length=100)
    number = models.IntegerField()
    city = models.CharField(max_length=30)
    block = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="address",
    )

    delivery_address = models.OneToOneField(
        "address.DeliveryAddress",
        on_delete=models.CASCADE,
        related_name="address",
        null=True,
        blank=True,
    )


class DeliveryAddress(models.Model):
    class Meta:
        ordering = ["id"]

    street = models.CharField(max_length=100)
    number = models.IntegerField()
    city = models.CharField(max_length=30)
    block = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    is_default = models.BooleanField(default=False)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="delivery_addresses",
    )
