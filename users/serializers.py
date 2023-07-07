from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from orders.models import Order
from products.models import Product
from shop_cart.models import CartProduct
from .models import User
from address.models import Address


class AddressSerializerInUser(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "street", "number", "city", "block", "zip_code", "is_default"]


class ProductSerializerInUser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock_quantity"]


class CartSerializerInUser(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ["product", "quantity", "total"]


class OrderSerializerInUser(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["status", "product_quantity"]


class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializerInUser(read_only=True, many=True)
    products = ProductSerializerInUser(read_only=True, many=True)
    shop_cart = ProductSerializerInUser(read_only=True, many=True)
    orders = OrderSerializerInUser(read_only=True, many=True)

    date_of_birth = serializers.DateField(input_formats=["%d-%m-%Y"])
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "date_of_birth",
            "password",
            "is_employee",
            "is_admin",
            "addresses",
            "products",
            "shop_cart",
            "orders",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
        extra_kwargs = {
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            "email": {"validators": [UniqueValidator(queryset=User.objects.all())]},
            "password": {"write_only": True},
        }

    def validate_date_of_birth(self, value):
        try:
            serializers.DateField().to_internal_value(value)
        except serializers.ValidationError:
            raise serializers.ValidationError(
                "Formato de data inválido. Use o formato 'dd-mm-aaaa'."
            )

        return value

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop("password")
        if password:
            instance.set_password(password)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
