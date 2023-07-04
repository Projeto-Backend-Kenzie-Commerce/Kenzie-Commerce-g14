from django.urls import path

from .views import AddressView, DeliveryAddressView, DeliveryaddressDetailView

urlpatterns = [
    path("users/<int:pk>/address/", AddressView.as_view()),
    path("users/<int:pk>/address/<int:id>/", AddressDetailView.as_view()),
]
