from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "price", "description", "stock_quantity"]
