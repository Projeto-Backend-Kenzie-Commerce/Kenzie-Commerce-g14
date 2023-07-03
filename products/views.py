from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



# class UserDetailView(RetrieveUpdateDestroyAPIView):
#     authentication_classes = [JWTAuthentication]
#     # permission_classes = [IsAccountOwner]

#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_url_kwarg = "pk"