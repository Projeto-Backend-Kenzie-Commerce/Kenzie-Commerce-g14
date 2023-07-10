from rest_framework import serializers

from .models import CartProduct, ShopCart
from products.serializers import ProductSerializer


class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    # total_product = serializers.SerializerMethodField(method_name="get_total_product")

    class Meta:
        model = CartProduct
        fields = ["cart_id", "product", "quantity"]

    # def get_total_product(self):
    #     return sum(cart_product.total for cart_product in self.cartproduct_set.all())

    def create(self, validated_data: dict) -> CartProduct:
        return CartProduct.objects.create(**validated_data)


class ShopCartSerializer(serializers.ModelSerializer):
    cart_product = CartProductSerializer(read_only=True)
    # products = CartProductSerializer(many=True, read_only=True)
    # subtotal = serializers.SerializerMethodField(method_name="get_subtotal")

    class Meta:
        model = ShopCart
        fields = ["id", "cart_product"]

    # def calculate_subtotal(self, obj: dict):
    #  obj.CartProduct.total_product = obj.products.price * obj.CartProduct.quantity

    def create(self, validated_data: dict) -> ShopCart:
        user = self.context["request"].user
        shop_cart = ShopCart.objects.create(user=user)
        return shop_cart


"""     def get_subtotal(self, obj: dict):
        subtotal_result = obj.CartProduct.total_product = (
            obj.products.price * obj.CartProduct.quantity
        )
        return subtotal_result """
