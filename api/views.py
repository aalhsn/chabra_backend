from rest_framework.generics import (
	CreateAPIView, RetrieveAPIView, ListAPIView, 
	RetrieveUpdateAPIView)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

import uuid

from .serializers import (
	UserCreateSerializer, ProductDetailsSerializer, ProductsListSerializer,
	UpdateProfileSerializer, OrderSerializer, AddressSerializer
)
from .models import (Product, Profile, Order, Basket, Address)


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer


class ProductListView(ListAPIView):
	queryset = Product.objects.filter(active=True)
	serializer_class = ProductsListSerializer


class ProductDetails(RetrieveAPIView):
	queryset = Product.objects.filter(active=True)
	serializer_class = ProductDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'product_id'


class ProfileUpdateView(RetrieveUpdateAPIView):
	serializer_class = UpdateProfileSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		return Profile.objects.get(user=self.request.user)

class AddressCreateAPIView(CreateAPIView):
	serializer_class = AddressSerializer


class OrderItems(APIView):
	serializer_class = OrderSerializer

	def post(self, request):
		rand_order_ref = str(uuid.uuid4())[0:8]
		total = 0
		for item in request.data['baskets']:
			total += item['quantity']*Product.objects.get(id=item['id']).price
		
		address_data = request.data['address']
		address_data["profile"] = request.user.profile
		address_object, _ = Address.objects.get_or_create(**address_data)
		address_object.save()

		order  = Order.objects.create(order_ref= rand_order_ref, customer = request.user, address= address_object, total=total)
		items = request.data['baskets']
		for item in items:
			Basket.objects.create(
				product_id=item['id'],
				quantity= item['quantity'],
				order=order
			)
		return Response(self.serializer_class(order).data, status=HTTP_200_OK)



