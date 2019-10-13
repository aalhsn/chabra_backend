from django.urls import path
from .views import UserCreateAPIView, ProductListView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('products/', ProductListView.as_view(), name='product-list'),
]