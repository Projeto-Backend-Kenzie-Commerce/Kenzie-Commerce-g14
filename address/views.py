from users.permissions import IsAccountOwner
from .models import Address
from .serializers import AddressSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView


class AddressView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_url_kwarg = "id"
