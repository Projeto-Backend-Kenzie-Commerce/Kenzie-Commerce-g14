from django.urls import path

from .views import CartProductView, CartView

urlpatterns = [
    path("product/<int:pk>/cart/", CartView.as_view()),
    path("product/<int:pk>/cart/buy/", CartProductView.as_view()),
]
