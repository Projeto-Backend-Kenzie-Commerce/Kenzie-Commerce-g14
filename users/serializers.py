from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User

from rest_framework import serializers
from address.models import Address


class AddressSerializerInUser(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "street",
            "number",
            "city",
            "block",
            "zip_code",
        ]


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializerInUser(read_only=True, default={})

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "is_employee",
            "is_admin",
            "address",
            "is_active",
        ]
        read_only_fields = ["id"]
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

    def get_address(self, obj):
        return obj.address

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
