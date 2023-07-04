from users.permissions import IsAccountOwner
from .models import Address, DeliveryAddress
from .serializers import AddressSerializer, DeliveryAddressSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


class AddressView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeliveryAddressView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = DeliveryAddressSerializer

    def get_queryset(self):
        return self.request.user.delivery_addresses.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeliveryaddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer
    lookup_url_kwarg = "pk"
