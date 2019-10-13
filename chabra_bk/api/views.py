
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from .serializers import UserCreateSerializer, ProductDetailsSerializer, ProductsListSerializer
from .models import Product


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer

class ProductDetails(RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'product_id'
	#permission_classes = [IsAuthenticated, IsBookingOwner]

