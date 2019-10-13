from django.urls import path
from .views import UserCreateAPIView, ProductDetails
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    #PRODUCTS
    path('detail/<int:product_id>/', ProductDetails.as_view(), name='product-detail'),

]