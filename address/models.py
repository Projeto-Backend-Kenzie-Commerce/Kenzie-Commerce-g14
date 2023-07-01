from django.db import models


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
