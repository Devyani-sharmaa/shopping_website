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





class Order(models.Model):
    product = models.ForeignKey(add_product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')])
