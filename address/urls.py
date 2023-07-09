from django.urls import path
from .views import AddressView, AddressDetailView


urlpatterns = [
    path("address/", AddressView.as_view()),
    path("address/<int:id>/", AddressDetailView.as_view()),
]
