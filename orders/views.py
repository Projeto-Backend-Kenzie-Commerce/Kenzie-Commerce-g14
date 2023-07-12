from .models import Order
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import OrderSerializer
from products.models import Product
from users.permissions import IsSellerOrAdmin, IsClient
from users.models import User
from django.shortcuts import get_object_or_404


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def get_queryset(self):
        if not self.request.user.is_employee:
            return Order.objects.filter(user=self.request.user)

        return Order.objects.filter(is_employee=self.request.user)

    def perform_create(self, serializer):
        products = serializer.validated_data.get("product", [])

        users = []
        for product in products:
            user = get_object_or_404(Product, id=product.id).user
            users.append(user)

        print(users)
        serializer.save(user=self.request.user, is_employee=users[0])


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdmin]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = "pk"

    def get_permissions(self):
        if self.request.method == "DELETE":
            lookup_value = self.kwargs.get(self.lookup_field)
            order = Order.objects.filter(id=lookup_value, user=self.request.user)
            if order.exists() and self.request.user.id == order[0].user.id:
                return [IsAuthenticated()]

        if self.request.method == "GET":
            return [IsClient()]

        return super().get_permissions()

    def perform_destroy(self, instance: Order):
        instance.status = "canceled"
        instance.save()
        instance.delete()

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
