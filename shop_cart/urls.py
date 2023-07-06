from django.urls import path
from .views import CartView

urlpatterns = [
    path("cart/product/<int:pk>/", CartView.as_view()),
    # path("cart/retrieve"),
]
