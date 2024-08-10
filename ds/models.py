from django.db import models

# Create your models here.


class add_product(models.Model):
     product_name=models.CharField( max_length=50)
     product_description=models.CharField( max_length=50)
     price=models.CharField( max_length=50)
     old_price=models.CharField( max_length=50)
     rating=models.CharField( max_length=50)
     out_of=models.CharField( max_length=50)
     image1=models.ImageField(upload_to="productimage",null=True,blank=True)
     image2=models.ImageField(upload_to="productimage",null=True,blank=True)
     image3=models.ImageField(upload_to="productimage",null=True,blank=True)
