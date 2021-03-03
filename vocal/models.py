from django.db import models
    
class HomeMakeOver(models.Model):
    name= models.CharField(max_length=100)
    img=models.ImageField(upload_to="Home")
    price= models.IntegerField(default=0)
    offer= models.IntegerField(default=0)
    desc=models.TextField(max_length=250,default=0)
   
    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'HomeMakeOver'
    
class BeautyProduct(models.Model):
    name= models.CharField(max_length=100)
    img=models.ImageField(upload_to="Beauty")
    price= models.IntegerField(default=0)
    offer= models.IntegerField(default=0)
    desc=models.TextField(max_length=250,default=0)

    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'BeautyProduct'

class SanityWare(models.Model):
    name= models.CharField(max_length=100)
    img=models.ImageField(upload_to="Sanitry")
    price= models.IntegerField(default=0)
    offer= models.IntegerField(default=0)
    desc=models.TextField(max_length=250,default=0)
    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'SanityWare'

class Stationary(models.Model):
    name= models.CharField(max_length=100)
    img=models.ImageField(upload_to="Stationary")
    price= models.IntegerField(default=0)
    offer= models.IntegerField(default=0)
    desc=models.TextField(max_length=250,default=0)
       
    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'Stationary'

# Create your models here.
class Products(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    Category=models.CharField(max_length=50, default="")
    Sub_Category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    product_Desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    product_image=models.ImageField(upload_to='media',default="")
    
    def __str__(self):
        return self.product_name
        
    class Meta:
        db_table = 'Products'