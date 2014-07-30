from django.db import models

# Create your models here.
class Customer(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	
	def __unicode__(self):
		return self.name

class Product(models.Model):
	title=models.CharField(max_length=500)
	image=models.ImageField(upload_to= 'media/')
	description=models.CharField(max_length=10000)
	price=models.FloatField()
	time=models.DateTimeField('date last edited')
	
	owner=models.ForeignKey(Customer,related_name="owner of Product")
	
	subscribers=models.ManyToManyField(Customer,related_name="list of subscribers")	
	placed_users=models.ManyToManyField(Customer,related_name="for placed_users")
	
	def __unicode__(self):
		return self.title
