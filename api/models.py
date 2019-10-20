from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver 

class Product(models.Model):
	name=models.CharField(max_length=120)
	# product_type=models.CharField(choices=TYPE, max_length=25) add later in category model
	price=models.DecimalField(max_digits=6, decimal_places=3, validators=[MinValueValidator(0.0)])
	img=models.ImageField()
	# origin= models.CharField(max_length=120) Add later in own model
	quantity=models.PositiveIntegerField()
	description=models.TextField()
	active=models.BooleanField(default=True) # changed from availability to active
	quantity_per_order=models.PositiveIntegerField()
	date_added=models.DateField(auto_now=True)


	def __str__ (self):
		return "[ %s ] %s" %(self.id,self.name)



GENDER = (("F", "Female"), ("M", "Male"))

class Profile(models.Model):
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

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()  

class Order(models.Model):
	order_ref = models.CharField(max_length=10)
	customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
	date_time = models.DateTimeField(auto_now_add=True)
	# address = models.CharField(max_length=100)


class Basket(models.Model):
	item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
	quantity = models.PositiveIntegerField()
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='ordered_items')


