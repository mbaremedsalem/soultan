from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name    

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category ,related_name='category',on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True)
    date_added = models.DateTimeField(auto_now=True)        

    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.title  
class Order(models.Model):
    product = models.ForeignKey(Product,related_name='apply_order',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)   
      
    def __str__(self):
        return self.name

