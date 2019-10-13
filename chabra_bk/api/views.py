from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import UserCreateSerializer, ProductDetailsSerializer

# Models
from .models import Product

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ProductDetails(RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'product_id'
	#permission_classes = [IsAuthenticated, IsBookingOwner]