from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

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
	phone = models.PositiveIntegerField(null=True, max_length=15)
	gender = models.CharField(choices=GENDER, max_length=25, null=True)
	age = models.PositiveIntegerField(null=True)
	image = models.ImageField(null=True)

	def __str__(self):
		return self.user.username