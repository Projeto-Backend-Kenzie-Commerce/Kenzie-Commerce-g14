from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsSellerOrAdmin, IsClientOrAdmin, IsAdmin


class ProductView(CreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSellerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "pk"

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsClientOrAdmin()]
        elif self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsSellerOrAdmin()]
        elif self.request.method == 'DELETE':
            return [IsSellerOrAdmin()]