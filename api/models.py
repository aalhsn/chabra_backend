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
	active=models.BooleanField(default=True) # changed from availability to active
	quantity_per_order=models.PositiveIntegerField()
	date_added=models.DateField(auto_now=True)


	def __str__ (self):
		#fix admin page
		return "[ %s ] %s" %(self.id,self.name)


class Profile(models.Model):
	GENDER = (("F", "Female"), ("M", "Male"))
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	phone = models.PositiveIntegerField(null=True, max_length=15)
	gender = models.CharField(choices=GENDER, max_length=1, null=True)
	age = models.PositiveIntegerField(null=True)
	image = models.ImageField(null=True)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user= instance)
