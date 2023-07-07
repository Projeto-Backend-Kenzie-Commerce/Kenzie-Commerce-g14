from rest_framework import serializers
from .models import Order
from django.shortcuts import get_object_or_404
from products.models import Product
from users.models import User
from rest_framework.exceptions import ValidationError
from django.conf import settings
from django.core.mail import send_mail


def mailing(product, email):
    send_mail(
        subject="Descrição do pedido - Kenzie commerce",
        message=f"Pedido do produto {product} foi confirmado, em breve o vendedor do produto colocará seu pedido para produção.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )


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
        user = validated_data.get("user")
        validated_data.pop("user")
        validated_data.pop("is_employee")
        quantity = validated_data.get("product_quantity")
        data_products = validated_data.pop("product", [])

        products = []
        for product in data_products:
            product = get_object_or_404(Product, id=product.id)
            if product.stock_quantity < quantity:
                raise ValidationError(
                    "quantity ordered is greater than quantity in stock"
                )
            product.stock_quantity = product.stock_quantity - quantity
            product.save()
            products.append(product)

        email = get_object_or_404(User, id=user.id)
        mailing(product=products[0].name, email=email.email)

        order = Order.objects.create(**validated_data)
        order.product.set(products)
        return order

    def update(self, instance: Order, validated_data: dict) -> Order:
        status = validated_data.get("status")
        if status:
            instance.status = status
            instance.save()
        return instance
