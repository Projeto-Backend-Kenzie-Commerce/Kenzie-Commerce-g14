from rest_framework.exceptions import ValidationError
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

    def validate(self, attrs: dict) -> dict:
        keys_exists = "is_default" in attrs
        if not keys_exists:
            attrs["is_default"] = True

        is_default = attrs.get("is_default", None)

        if is_default:
            user_id = self.context["request"].user.id
            has_default_address = Address.objects.filter(
                user_id=user_id, is_default=True
            ).first()

            if has_default_address:
                has_default_address.is_default = False
                has_default_address.save()
        else:
            user_id = self.context["request"].user.id
            if self.instance:
                address_id = self.instance.id

                has_default_address = Address.objects.filter(
                    user_id=user_id, is_default=True
                ).first()

                if not has_default_address:
                    raise serializers.ValidationError(
                        {
                            "message": "Pelo menos um endereço deve ser definido como padrão."
                        }
                    )
                if address_id == has_default_address.id:
                    raise serializers.ValidationError(
                        {
                            "message": "Pelo menos um endereço deve ser definido como padrão."
                        }
                    )
            has_default_address = Address.objects.filter(
                user_id=user_id, is_default=True
            ).exists()

            if not has_default_address:
                raise serializers.ValidationError(
                    {"message": "Pelo menos um endereço deve ser definido como padrão."}
                )

        return attrs

    def create(self, validated_data: dict) -> Address:
        return Address.objects.create(**validated_data)


#  fazer as rotas no insomnia com employee e sem employee com admin e sem admin
