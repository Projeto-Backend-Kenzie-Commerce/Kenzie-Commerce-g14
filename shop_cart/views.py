from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from products.models import Product
from .models import ShopCart, CartProduct
from .serializers import CartProductSerializer, ShopCartSerializer
from rest_framework.permissions import IsAuthenticated


class CartProductView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        user = self.request.user

        try:
            shop_cart = user.shop_cart
        except ShopCart.DoesNotExist:
            shop_cart = ShopCart.objects.create(user=user)

        product = Product.objects.get(pk=pk)
        shop_cart.products.add(product)
        shop_cart.save()

        serializer = ShopCartSerializer(shop_cart)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        user = self.request.user

        shop_cart = ShopCart.objects.get(user=user)

        cart_shop = shop_cart.products.filter(id=pk).first()

        shop_cart.products.remove(cart_shop)
        shop_cart.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
