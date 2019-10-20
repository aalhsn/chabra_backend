from rest_framework.generics import (CreateAPIView, RetrieveAPIView, ListAPIView)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
from rest_framework.response import Response
import uuid

from .serializers import (UserCreateSerializer, ProductDetailsSerializer, ProductsListSerializer,
	ProfileSerializer, OrderSerializer)

from .models import (Product, Profile, Order, Basket)


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class ProductListView(ListAPIView):
	queryset = Product.objects.filter(active=True)
	serializer_class = ProductsListSerializer

class ProductDetails(RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'product_id'

class ProfileView(RetrieveAPIView):
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated]

	def get(self, request, format=None):
		if request.user.is_anonymous:
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
		profile = ProfileSerializer(Profile.objects.get(user=request.user))
		return Response(profile.data, status=HTTP_200_OK)

	
class OrderList(ListAPIView):
	serializer_class = OrderSerializer

	def get_queryset(self):
		query = Order.objects.filter(customer=self.request.user)
		return query

class OrderItems(APIView):

	def post(self, request):
		rand_order_ref = str(uuid.uuid4())[0:8]
		order  = Order.objects.create(order_ref= rand_order_ref, customer = request.user)
		items = request.data
		for item in items:
			basket = Basket.objects.create(item = Product.objects.get(id=item['id']), quantity= item['quantity'] , order= order)
		return Response(order.id, status=HTTP_200_OK)

	def get(self, request):
		orders = OrderSerializer(Order.objects.filter(customer=self.request.user), many=True)
		return Response(orders.data,status=HTTP_200_OK)


