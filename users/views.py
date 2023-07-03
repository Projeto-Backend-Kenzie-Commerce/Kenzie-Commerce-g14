from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from .serializers import UserSerializer
from .permissions import IsAccountOwner


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "pk"


# Sobrescrever o metodo post pq o createAPIView ele só cria uma instancia de order por vez
# e precismaos criar varias de uma vez só

# Criar 2 colunas uma para a order comprada e a order vendida pq o user pode se vendedor tbm.
# voltar o total_price e quantidade de produtos total na order com serializerMethodField.
