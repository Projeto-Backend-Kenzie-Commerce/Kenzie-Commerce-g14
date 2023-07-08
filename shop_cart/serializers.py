from rest_framework import serializers
from .models import ShopCart
from products.serializers import ProductSerializer
from users.serializers import UserSerializer


""" class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    total_product = serializers.SerializerMethodField(method_name="get_total_product")

    class Meta:
        model = CartProduct
        fields = ("product", "quantity", "total_product")

    def get_total_product(self):
        return sum(cart_product.total for cart_product in self.cartproduct_set.all())

    def create(self, validated_data: dict) -> CartProduct:
        return CartProduct.objects.create(**validated_data) """


class ShopCartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    # products = CartProductSerializer(many=True, read_only=True)
    # subtotal = serializers.SerializerMethodField(method_name="get_subtotal")

    class Meta:
        user = UserSerializer(read_only=True)
        model = ShopCart
        fields = ["products", "user_id"]

    # def calculate_subtotal(self, obj: dict):
    #  obj.CartProduct.total_product = obj.products.price * obj.CartProduct.quantity

    def create(self, validated_data: dict) -> ShopCart:
        return ShopCart.objects.create(**validated_data)


"""     def get_subtotal(self, obj: dict):
        subtotal_result = obj.CartProduct.total_product = (
            obj.products.price * obj.CartProduct.quantity
        )
        return subtotal_result """
