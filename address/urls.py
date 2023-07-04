from django.urls import path

from .views import AddressView, DeliveryAddressView, DeliveryaddressDetailView

urlpatterns = [path("users/<int:pk>/address/", AddressView.as_view())]

urlpatterns = [
    path("users/<int:pk>/address/delivery/", DeliveryAddressView.as_view()),
    path(
        "users/<int:pk>/address/delivery/<int:pk>/", DeliveryaddressDetailView.as_view()
    ),
]
