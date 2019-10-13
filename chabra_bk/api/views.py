from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, ProductsListSerializer
from .models import Product


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer