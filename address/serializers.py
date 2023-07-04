from rest_framework import serializers
from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(method_name="get_username")
    email = serializers.SerializerMethodField(method_name="get_email")

    class Meta:
        model = Address
        fields = [
            "id",
            "username",
            "email",
            "street",
            "number",
            "city",
            "block",
            "zip_code",
            "is_default",
            "user_id",
        ]

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    def create(self, validated_data: dict) -> Address:
        return Address.objects.create(**validated_data)
