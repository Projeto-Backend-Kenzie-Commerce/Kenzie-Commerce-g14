from rest_framework import serializers
from .models import Product
from users.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'stock_quantity', 'user_id']

    def create(self, validated_data: dict) -> Product:
        return Product.objects.create(**validated_data)