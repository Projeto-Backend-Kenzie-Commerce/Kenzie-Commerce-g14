from django.urls import path

from address.views import AddressView

urlpatterns = [path("users/<int:pk>/address/", AddressView.as_view())]
