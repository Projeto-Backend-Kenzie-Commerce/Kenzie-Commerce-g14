from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CartProduct, ShopCart
from .serializers import CartSerializer
from users.permissions import IsClientOrAdmin


class CartView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = CartSerializer
    permission_classes = [IsClientOrAdmin]
    lookup_field = "pk"

    def get_object(self):
        return ShopCart.objects.get(user=self.request.user)
