from django.urls import path
from .views import CartView

urlpatterns = [path("product/<int:pk>/cart/", CartView.as_view())]
