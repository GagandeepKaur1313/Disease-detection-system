from django.db import models

# Create your models here.
'''
class person(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
'''
class doctors(models.Model):
	name=models.CharField(max_length=100)
	qualification=models.CharField(max_length=100)
	experience=models.CharField(max_length=30)
	hospital=models.CharField(max_length=100)
	image=models.ImageField(upload_to="data",blank=True)
	def __str__(self):
		return self.name

class blogs(models.Model):
	title=models.CharField(max_length=200)
	description=models.CharField(max_length=2000)
	image=models.ImageField(upload_to="data",blank=True)
	pub_date=models.DateTimeField('date published')
	creator=models.CharField(max_length=100)
	def __str__(self):
		return self.title

class review(models.Model):
	title=models.CharField(max_length=100)
	message=models.TextField(max_length=1000)
	def __str__(self):
		return self.title

class contactus(models.Model):
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	email=models.EmailField(max_length=50)
	phone=models.CharField(max_length=20)
	message=models.TextField(max_length=500)
	def __str__(self):
		return self.firstname

class userregister(models.Model):
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	email=models.EmailField(max_length=50)
	password=models.CharField(max_length=50)
	bio=models.CharField(max_length=500,blank=True,null=True)
	age=models.CharField(max_length=10,blank=True,null=True)
	pincode=models.CharField(max_length=10,blank=True,null=True)
	contact=models.CharField(max_length=20,blank=True,null=True)
	date=models.CharField(max_length=20,blank=True,null=True)
	address=models.CharField(max_length=200,blank=True,null=True)
	image=models.ImageField(upload_to="data",blank=True,null=True)
	def __str__(self):
		return self.firstname

class helpus(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField(max_length=1000)
	def __str__(self):
		return self.title
