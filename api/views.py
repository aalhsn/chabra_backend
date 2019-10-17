from rest_framework.generics import (CreateAPIView, RetrieveAPIView, ListAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
from rest_framework.response import Response

from .serializers import (UserCreateSerializer, ProductDetailsSerializer, ProductsListSerializer, 
	ProfileSerializer)

from .models import (Product, Profile)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

# filter items by active status
class ProductListView(ListAPIView):
    queryset = Product.objects.filter(active= True)
    serializer_class = ProductsListSerializer

# filter items by active status
class ProductDetails(RetrieveAPIView):
	queryset = Product.objects.filter(active= True)
	serializer_class = ProductDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'product_id'


class ProfileView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		profile = ProfileSerializer(request.user.profile)
		return Response(profile.data, status=HTTP_200_OK)

	
