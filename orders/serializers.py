from rest_framework import serializers
from .models import StatusChoices


class Order(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.ChoiceField(choices=StatusChoices.choices)
    product_quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
