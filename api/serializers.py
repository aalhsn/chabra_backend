from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Profile, Basket, Order

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(username=username)
		new_user.set_password(password)
		new_user.save()
		return validated_data


class ProductsListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id', 'name', 'price', 'img', 'date_added']



class ProductDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id', 'name', 'price', 'img','quantity', 'description',
				 'active', 'quantity_per_order', 'date_added']


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "email"]


class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Profile
		fields = '__all__'

class BasketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Basket
		fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
	ordered_items= BasketSerializer(many=True)

	class Meta:
		model = Order
		fields = ["order_ref", "customer", "address", "ordered_items"]

	def create(self, validated_data):
		return Basket.objects.create(validated_data)
		