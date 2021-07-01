from django.db import models

# Create your models here.
class ProductItem(models.Model):
     item=models.CharField(max_length=30)
     def __str__(self):
         return self.item
     
class Productdb(models.Model):
    pname=models.CharField(max_length=30)
    pdesc=models.CharField(max_length=200)
    pprice=models.FloatField()
    pdiscount=models.FloatField()
    pimg=models.ImageField(upload_to='product/%y/%m/%d')
    item=models.ForeignKey(ProductItem,on_delete=models.CASCADE)
    
    

