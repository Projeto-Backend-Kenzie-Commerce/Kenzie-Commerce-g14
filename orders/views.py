from .models import Order
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .serializers import OrderSerializer
from users.permissions import IsSellerOrAdmin, IsClient
from users.models import User
from django.shortcuts import get_object_or_404


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdmin]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsSellerOrAdmin()]
        else:
            return [IsClient()]

    def get_queryset(self):
        return Order.objects.filter(is_employee=self.request.user)

    def perform_create(self, serializer):
        data_user = serializer.validated_data.get("user")
        data_seller = serializer.validated_data.get("is_employee")
        data_products = serializer.validated_data.get("product")
        print(data_seller)
        user = get_object_or_404(User, id=data_user.id)
        seller = get_object_or_404(User, id=data_seller.id, is_employee=True)

        serializer.save(user_id=user.id, is_employee_id=seller.id)
