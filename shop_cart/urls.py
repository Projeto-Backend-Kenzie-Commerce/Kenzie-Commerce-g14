from django.urls import path

from .views import CartProductView

urlpatterns = [
    path("product/<int:pk>/cart/buy/", CartProductView.as_view()),
]
