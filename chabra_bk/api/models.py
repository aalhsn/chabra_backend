from django.db import models
from django.contrib.auth.models import User



# class Category(models.Model):
# 	name=models.CharField(max_length=120)
# 	subcategories= models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='subcategory')

class Subcategory(models.Model):
	name=models.CharField(max_length=120)
	# Category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

class Product(models.Model):
	name=models.CharField(max_length=120)
	subcategory=models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='related')
	price=models.PositiveIntegerField()
	img=models.ImageField()
	brand_name= models.CharField(max_length=120)
	quantity=models.PositiveIntegerField()
	description=models.TextField()
	availibility=models.BooleanField(default=True)
	quantity_per_order=models.PositiveIntegerField()
	date_added=models.DateField()





GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	phone=models.PositiveIntegerField()
	gender=models.CharField(choices=GENDER, max_length=25)
	age=models.PositiveIntegerField()
	img=models.ImageField()



PAYMENT_METHOD = (
    ('CASH', 'Cash on delivery'),
    ('KNET', 'K-Net')
)

STATUS = (
	('PENDING', 'Order is Pending'),
    ('CONIFORM', 'Order is Confirmed')
)

class Order(models.Model):
	number=models.PositiveIntegerField()
	products= models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ordereditems')
	total_price=models.PositiveIntegerField()
	user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='ordering')
	date=models.DateField()
	payment_method=models.CharField(choices=PAYMENT_METHOD, max_length=25)
	shipping_address=models.TextField()
	status=models.CharField(choices=STATUS, max_length=25)



class Cart(models.Model):
	user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
	products= models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartitems')
	date=models.DateField()
