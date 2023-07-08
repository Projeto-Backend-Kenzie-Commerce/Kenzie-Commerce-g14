from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsSellerOrAdmin, IsClientOrAdmin
from .models import Product
from .serializers import ProductSerializer


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSellerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self, **kwargs):
        filtro_name = self.request.query_params.get("name")
        filtro_category = self.request.query_params.get("category")

        if filtro_name:
            return Product.objects.filter(name__icontains=filtro_name)

        elif filtro_category:
            return Product.objects.filter(category__iexact=filtro_category)

        return super().get_queryset()


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "pk"

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsClientOrAdmin()]
        elif self.request.method == "PUT" or self.request.method == "PATCH":
            return [IsSellerOrAdmin()]
        elif self.request.method == "DELETE":
            return [IsSellerOrAdmin()]


# class CreateCustomerReviewView(ListCreateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     serializer_class = CustomerReviewSerializer

#     def get_queryset(self):
#         product_id = self.kwargs["pk"]
#         return Product.objects.filter(id=product_id)

#     def perform_create(self, serializer):
#         product_id = self.kwargs["pk"]
#         product = Product.objects.get(id=product_id)
#         serializer.save(user=self.request.user, product=product)
