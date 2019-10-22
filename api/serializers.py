from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Profile, Basket, Order

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self, validated_data):
		new_user = User(**validated_data)
		new_user.set_password(validated_data['password'])
		new_user.save()
		return validated_data


class ProductsListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id', 'name', 'price', 'img', 'date_added']

class ProductHistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['name', 'price']

class ProductDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id', 'name', 'price', 'img','quantity', 'description',
				 'active', 'date_added']


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "email"]
		read_only_fields = ['username']



class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Profile
		exclude = ["id"]


class UpdateProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Profile
		exclude = ["id"]

	def update(self, instance, validated_data):
		# removing (user) key from validated_data dictionary to use update the user which
		# has read only username field 
		user_field = validated_data.pop('user', None)
		temp_user_serializer = UserSerializer()
		super().update(instance, validated_data)
		super(UserSerializer, temp_user_serializer).update(instance.user, user_field)
		return instance



class BasketSerializer(serializers.ModelSerializer):
	product = ProductHistorySerializer()
	class Meta:
		model = Basket
		fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
	baskets= BasketSerializer(many=True)

	class Meta:
		model = Order
		fields = ["id", "order_ref", "customer", "address",  "baskets", "date_time", "total"]
		