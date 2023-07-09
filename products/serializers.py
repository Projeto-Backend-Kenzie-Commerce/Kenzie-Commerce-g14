from rest_framework import serializers
from .models import Product


# class CustomerReviewSerializer(serializers.ModelSerializer):
#     username = serializers.SerializerMethodField(method_name="get_username")

#     class Meta:
#         model = CustomerReview
#         fields = [
#             "id",
#             "username",
#             "rating",
#             "comment",
#             "user_id",
#             "created_at",
#         ]

#     def get_username(self, obj):
#         return obj.user.username

#     def create(self, validated_data):
#         return CustomerReview.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    # customer_reviews = CustomerReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Product

        fields = [
            "id",
            "name",
            "price",
            "description",
            "stock_quantity",
            "category",
            "created_at",
            "is_available",
            "user_id",
        ]

        read_only_fields = ["is_available"]

    # def validate(self, attrs: dict):
    #     quantity = "stock_quantity" in attrs
    #     available = "is_available" in attrs

    #     if quantity == 0:
    #         available = False

    #     return attrs

    def create(self, validated_data: dict) -> Product:
        return Product.objects.create(**validated_data)
