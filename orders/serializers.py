from rest_framework import serializers
from .models import Order
from django.shortcuts import get_object_or_404
from products.models import Product
from users.models import User
from rest_framework.exceptions import ValidationError
from django.conf import settings
from django.core.mail import send_mail


def mailing(product, email, message):
    send_mail(
        subject="Descrição do pedido - Kenzie commerce",
        message=message,
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
            "deleted",
        ]
        read_only_fields = ["id", "created_at", "deleted", "user", "is_employee"]

    def create(self, validated_data: dict) -> Order:
        user = self.context.get("request").user
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
        mailing(
            product=products[0].name,
            email=email.email,
            message=f"Pedido do produto {products[0]} foi confirmado, em breve o vendedor do produto colocará seu pedido para produção.",
        )

        order = Order.objects.create(**validated_data)
        order.product.set(products)
        return order

    def update(self, instance: Order, validated_data: dict) -> Order:
        status = validated_data.get("status")
        if status:
            instance.status = status
            instance.save()

        message = ""
        if status == "delivered":
            message = "entrege, obrigado por comprar conosco!"
        else:
            message = "colocado em produção, aguarde novas atualizações."

        mailing(
            product=instance.product.first().name,
            email=instance.user.email,
            message=f"Pedido do produto {instance.product.first().name} foi {message}",
        )

        return instance
