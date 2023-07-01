from rest_framework import serializers
from users.models import User

from users.serializers import UserSerializer


class AddressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data: dict) -> User:
        return User.objects.create(**validated_data)
