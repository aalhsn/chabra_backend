from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

TYPE = (
	('F', 'Fruit'),
	('V', 'Vegetable')
)

class Product(models.Model):
	name=models.CharField(max_length=120)
	product_type=models.CharField(choices=TYPE, max_length=25)
	price = models.DecimalField(max_digits=6, decimal_places=3, validators=[MinValueValidator(0.0)])
	img=models.ImageField()
	origin= models.CharField(max_length=120)
	quantity=models.PositiveIntegerField()
	description=models.TextField()
	availibility=models.BooleanField(default=True)
	quantity_per_order=models.PositiveIntegerField()
	date_added=models.DateField()

	def __str__ (self):
		return "[ %s ] %s" %(self.id,self.name)