from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductView.as_view()),
    path("product/<int:pk>/", views.ProductDetailView.as_view()),
    # path(
    #     "products/<int:pk>/reviews/",
    #     views.CreateCustomerReviewView.as_view(),
    #     name="create-review",
    # ),
]
