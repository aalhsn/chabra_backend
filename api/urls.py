from django.urls import path

from .views import (UserCreateAPIView, ProductDetails, ProductListView, ProfileUpdateView, OrderItems, AddressCreateAPIView)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:product_id>/', ProductDetails.as_view(), name='product-detail'),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
    path("orders/", OrderItems.as_view(), name="order-items"),
    path("address/", AddressCreateAPIView.as_view(), name="order-items"),

]