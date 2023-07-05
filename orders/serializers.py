from rest_framework import serializers
from .models import StatusChoices, Order
from django.shortcuts import get_object_or_404
from products.models import Product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "product_quantity",
            "user",
            "is_employee",
            "product",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data: dict) -> Order:
        validated_data.pop("user")
        validated_data.pop("is_employee")
        data_products = validated_data.pop("product", [])

        products = []
        for product in data_products:
            product = get_object_or_404(Product, id=product.id)
            products.append(product)

        order = Order.objects.create(**validated_data)
        order.product.set(products)
        return order
