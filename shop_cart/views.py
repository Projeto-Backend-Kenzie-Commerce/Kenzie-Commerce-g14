from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from products.models import Product
from .models import ShopCart, CartProduct
from .serializers import CartProductSerializer, ShopCartSerializer
from rest_framework.permissions import IsAuthenticated


class CartView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ShopCart.objects.all()
    serializer_class = ShopCartSerializer


class CartProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
    lookup_url_kwarg = "pk"

    def perform_create(self, serializer):
        user = self.request.user
        product_id = self.kwargs["pk"]

        try:
            shop_cart = user.shop_cart
        except ShopCart.DoesNotExist:
            shop_cart = ShopCart.objects.create(user=user)

        product = Product.objects.get(pk=product_id)
        cart_product, created = CartProduct.objects.get_or_create(
            cart=shop_cart, product=product
        )

        serializer.save(cart=shop_cart, product=cart_product)

    # def add_products_to_cart(request):
    #     user = request.user
    #     products = Product.objects.all()

    #     if products:
    #         cart, created = ShopCart.objects.get_or_create(user=user)

    #         for product_data in products:
    #             product = Product.objects.create(**product_data)
    #             cart_product = CartProduct.objects.create(cart=cart, product=product)
    #             # Define a quantidade e o total com base nas informações da API
    #             cart_product.quantity = product_data["quantity"]
    #             cart_product.total = product_data["total"]
    #             cart_product.save()

    #             return ShopCart.objects.all()
    #         else:
    #             return ShopCart.objects.all()
