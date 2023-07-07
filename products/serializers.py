from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = ['id', 'name', 'price', 'description', 'stock_quantity', 'created_at', 'user_id', 'is_available']

        read_only_fields = ['is_available']


    def validate(self, attrs: dict):
        quantity = "stock_quantity" in attrs
        available = "is_available" in attrs

        if quantity == 0:
            available = False
        
        return attrs
    
    
    def create(self, validated_data: dict) -> Product:
        return Product.objects.create(**validated_data)
