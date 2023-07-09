from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import ShopCart
from .serializers import ShopCartSerializer
from rest_framework.permissions import IsAuthenticated


class CartView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ShopCart.objects.all()
    serializer_class = ShopCartSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


""" def add_products_to_cart(request):
    user = request.user
    products = Product.objects.all()

    if products:
        cart, created = ShopCart.objects.get_or_create(user=user)

        for product_data in products:
            product = Product.objects.create(**product_data)
            cart_product = CartProduct.objects.create(cart=cart, product=product)
            # Define a quantidade e o total com base nas informações da API
            cart_product.quantity = product_data["quantity"]
            cart_product.total = product_data["total"]
            cart_product.save()

            return ShopCart.objects.all()
        else:
            return ShopCart.objects.all() """
