from django.urls import path
from .views import OrderView, OrderDetailView, OrderSelledView

urlpatterns = [
    path("orders/", OrderView.as_view()),
    path("orders/<int:pk>/", OrderDetailView.as_view()),
    path("orders/selled/", OrderSelledView.as_view()),
]
