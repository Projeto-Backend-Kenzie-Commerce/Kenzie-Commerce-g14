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

    def update(self, instance: Address, validated_data: dict) -> Address:
        user_id = self.context["view"].kwargs["pk"]

        has_default_address = Address.objects.filter(
            user_id=user_id, is_default=True
        ).exists()

        if has_default_address:
            Address.objects.filter(user_id=user_id).update(is_default=False)

        if "is_default" in validated_data and validated_data["is_default"]:
            validated_data["is_default"] = not has_default_address

        return super().update(instance, validated_data)


#  para fazer a lógica do default eu vou usar o update e fazer o segunte
#  verificar se existe o defult true, então antes de ele atualizar eu coloco todos como false,
# e deixo o novo que foi adicionado/atualizado como true depois da att.
