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


# ORDER Sobrescrever o metodo post pq o createAPIView ele só cria uma instancia de order por vez
# e precismaos criar varias de uma vez só

# Criar 2 colunas uma para a order comprada e a order vendida pq o user pode se vendedor tbm.
# voltar o total_price e quantidade de produtos total na order com serializerMethodField.


# class ProductView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsSellerOrAdmin]  # Apenas vendedores ou administradores podem cadastrar produtos


# class ProductDetailView(RetrieveUpdateDestroyAPIView):
#     authentication_classes = [JWTAuthentication]
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_url_kwarg = "pk"

#     def get_permissions(self):
#         if self.request.method == 'GET':
#             return [IsClientOrAdmin()]  # Apenas clientes ou administradores podem visualizar
#         elif self.request.method == 'PUT' or self.request.method == 'PATCH':
#             return [IsSellerOrAdmin()]  # Apenas vendedores ou administradores podem atualizar
#         elif self.request.method == 'DELETE':
#             return [IsAdmin]  # Apenas administradores podem excluir


# class OrderView(ListAPIView):
#     serializer_class = OrderSerializer
#     permission_classes = [IsSellerOrAdmin]  # Apenas vendedores ou administradores podem visualizar todos os pedidos vendidos

#     def get_queryset(self):
#         return Order.objects.filter(seller=self.request.user)


# class CartView(RetrieveUpdateAPIView):
#     authentication_classes = [JWTAuthentication]
#     serializer_class = CartSerializer
#     permission_classes = [IsClientOrAdmin]  # Apenas clientes ou administradores podem adicionar produtos ao carrinho

#     def get_object(self):
#         return Cart.objects.get(user=self.request.user)


# class OrderClientView(ListAPIView):
#     authentication_classes = [JWTAuthentication]
#     serializer_class = OrderSerializer
#     permission_classes = [IsClientOrAdmin]  # Apenas clientes ou administradores podem visualizar todos os pedidos comprados

#     def get_queryset(self):
#         return Order.objects.filter(client=self.request.user)
