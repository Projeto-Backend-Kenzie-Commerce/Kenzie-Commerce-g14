from rest_framework import serializers
from .models import StatusChoices, Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "product_quantity",
            "user_id",
            "is_employee_id",
            "product_id",
            "created_at",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> Order:
        return Order.objects.create(**validated_data)
