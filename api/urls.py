from django.urls import path

from .views import (UserCreateAPIView, ProductDetails, ProductListView, ProfileView, ProfileUpdateView, OrderList, OrderItems)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    
    # Auth
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),

    # Products List
    path('products/', ProductListView.as_view(), name='product-list'),

    # Products Details
    path('products/<int:product_id>/', ProductDetails.as_view(), name='product-detail'),

    # User Profile
    path("profile/", ProfileView.as_view(), name="profile"),

    #Update Profile
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile-edit"),

    #Order
    path("order/", OrderList.as_view(), name="order"),

    #Order Items
    path("items/", OrderItems.as_view(), name="order-items"),



]