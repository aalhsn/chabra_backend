from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver 


class Product(models.Model):
	name=models.CharField(max_length=120)
	price=models.DecimalField(max_digits=6, decimal_places=3, validators=[MinValueValidator(0.0)])
	img=models.ImageField()
	stock=models.PositiveIntegerField()
	description=models.TextField()
	active=models.BooleanField(default=True)
	date_added=models.DateField(auto_now=True)

	def __str__ (self):
		return self.name


class Profile(models.Model):
	GENDER = (
		("F", "Female"),
		("M", "Male")
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	phone = models.PositiveIntegerField(null=True)
	gender = models.CharField(choices=GENDER, max_length=2, null=True)
	age = models.PositiveIntegerField(null=True)
	image = models.ImageField(null=True)


	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user= instance)

class Address(models.Model):
	area = models.CharField(max_length=150)
	street = models.CharField(max_length=200)
	block = models.CharField(max_length=50)
	optional = models.CharField(max_length=200)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='addresses')

class Order(models.Model):
	order_ref = models.CharField(max_length=10)
	address = models.CharField(max_length=200)
	customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
	date_time = models.DateTimeField(auto_now_add=True)
	total = models.DecimalField(max_digits=8, decimal_places=3, validators=[MinValueValidator(0.0)])

@receiver(post_save, sender=Order)
def save_new_address(instance, created, **kwargs):
	if created:
		profile = Profile.objects.get(user=instance.customer)
		print(">>>>>HERHE   ",profile.addresses)
		if profile.addresses == True:
			for address in profile.addresses:
				if instance.address.area != address.area and instance.address.street != address.street and instance.address.block != address.block:
					profile.addresses.append(instance.address)
					profile.save()
		else :

			profile.addresses.append(instance.address)
			profile.save()



class Basket(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
	quantity = models.PositiveIntegerField()
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='baskets')

@receiver(post_save, sender=Basket)
def reduce_inventory(instance, created, **kwargs):
	if created:
		product = Product.objects.get(id=instance.product.id)
		product.stock -= instance.quantity
		product.save()
