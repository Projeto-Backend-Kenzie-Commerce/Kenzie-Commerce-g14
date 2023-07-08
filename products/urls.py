from django.urls import path
from . import views

urlpatterns = [
    path("users/<int:pk>/products/", views.ProductView.as_view()),
    path("users/products/<int:pk>/", views.ProductDetailView.as_view())
    # path(
    #     "products/<int:pk>/reviews/",
    #     views.CreateCustomerReviewView.as_view(),
    #     name="create-review",
    # ),
]
