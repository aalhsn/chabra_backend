from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Product



#Used for Register
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


class ProductDetailsSerializer(serializers.ModelSerializer):
	#total = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = ['name', 'product_type', 'price', 'img', 'origin',
					'quantity', 'description', 'availibility', 'quantity_per_order', 'date_added']


#Used for Login
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

