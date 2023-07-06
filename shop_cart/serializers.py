from rest_framework import serializers
from .models import ShopCart, CartProduct
from products.serializers import ProductSerializer


class CartProductSerializer(serializers.Serializer):
    prodduct = ProductSerializer(read_only=True)

    class Meta:
        model = CartProduct
        fields = ("product", "quantity", "total")


class CartSerializer(serializers.Serializer):
    products = CartProductSerializer(many=True, read_only=True)
    subtotal = serializers.DecimalField(decimal_places=2, max_digits=5, read_only=True)

    class Meta:
        model = ShopCart
        fiels = ("products", "subtotal")
