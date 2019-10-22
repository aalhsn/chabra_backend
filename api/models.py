from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver 

class Product(models.Model):
	name=models.CharField(max_length=120)
	price=models.DecimalField(max_digits=6, decimal_places=3, validators=[MinValueValidator(0.0)])
	img=models.ImageField()
	quantity=models.PositiveIntegerField()
	description=models.TextField()
	active=models.BooleanField(default=True)
	date_added=models.DateField(auto_now=True)
	origin = models.CharField(max_length=50)
	


	def __str__ (self):
		return self.name


class Profile(models.Model):
	GENDER = (
		("F", "Female"),
		("M", "Male")
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	phone = models.PositiveIntegerField(null=True)
	gender = models.CharField(choices=GENDER, max_length=25, null=True)
	age = models.PositiveIntegerField(null=True)
	image = models.ImageField(null=True)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user= instance)


class Order(models.Model):
	order_ref = models.CharField(max_length=10)
	address = models.CharField(max_length=200)
	customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
	date_time = models.DateTimeField(auto_now_add=True)
	total = models.DecimalField(max_digits=8, decimal_places=3, validators=[MinValueValidator(0.0)])


class Basket(models.Model):
	# Change field name to product
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
	quantity = models.PositiveIntegerField()
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='baskets')


