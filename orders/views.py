from .models import Order
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import OrderSerializer
from users.permissions import IsSellerOrAdmin, IsClient, IsOwnerOrAdmin
from users.models import User
from django.shortcuts import get_object_or_404


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        if not self.request.user.is_employee:
            return Order.objects.filter(user=self.request.user)

        return Order.objects.filter(is_employee=self.request.user)

    def perform_create(self, serializer):
        data_user = serializer.validated_data.get("user")
        data_seller = serializer.validated_data.get("is_employee")
        print(data_seller)
        user = get_object_or_404(User, id=data_user.id)
        seller = get_object_or_404(User, id=data_seller.id, is_employee=True)

        serializer.save(user_id=user.id, is_employee_id=seller.id)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdmin]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = "pk"

    def get_permissions(self):
        lookup_value = self.kwargs.get(self.lookup_field)
        order = Order.objects.filter(id=lookup_value, user=self.request.user)
        if self.request.method == "DELETE" and self.request.user.id == order[0].id:
            return IsOwnerOrAdmin

    def perform_destroy(self, instance: Order):
        instance.status = "canceled"
        instance.save()
        instance.delete()

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsClient()]

        return super().get_permissions()

    def get_queryset(self):
        lookup_value = self.kwargs.get(self.lookup_field)
        if not self.request.user.is_employee:
            return Order.objects.filter(id=lookup_value, user=self.request.user)

        return Order.objects.filter(id=lookup_value)


class OrderSelledView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdmin]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(status="delivered")


class OrderCancelView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        if not self.request.user.is_employee:
            return Order.objects.all(force_visibility=True).filter(
                status="canceled", user=self.request.user
            )

        return Order.objects.all(force_visibility=True).filter(status="canceled")
