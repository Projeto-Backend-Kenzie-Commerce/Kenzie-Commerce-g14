from rest_framework import serializers
from address.models import Address, DeliveryAddress


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = [
            "street",
            "number",
            "city",
            "block",
            "zip_code",
            "is_default",
        ]


class AddressSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(method_name="get_username")
    email = serializers.SerializerMethodField(method_name="get_email")

    class Meta:
        model = Address
        fields = [
            "username",
            "email",
            "street",
            "number",
            "city",
            "block",
            "zip_code",
            "delivery_address",
            "user_id",
        ]

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    def create(self, validated_data: dict) -> Address:
        delivery_address_data = validated_data.pop("delivery_address", {})
        address = Address.objects.create(**validated_data)

        if delivery_address_data:
            delivery_address = DeliveryAddress.objects.create(
                address=address, **delivery_address_data
            )
            address.delivery_address = delivery_address

        address.save()
        return address
