from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.


class add_product(models.Model):
     product_name=models.CharField( max_length=50)
     product_description=models.CharField( max_length=50)
     price=models.CharField( max_length=50)
     old_price=models.CharField( max_length=50)
     rating=models.CharField( max_length=50)
     out_of=models.CharField( max_length=50)
     image1=models.ImageField(upload_to="productimage",null=True,blank=True)
    #  image2=models.ImageField(upload_to="productimage",null=True,blank=True)
    #  image3=models.ImageField(upload_to="productimage",null=True,blank=True)

 



class Order(models.Model):
    product = models.ForeignKey(add_product, on_delete=models.CASCADE)
    # l.price=models.CharField( max_length=50)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')])





# class User(AbstractUser):

#      email = models.EmailField(unique=True)

#      username = models.CharField(max_length=100)


#      USERNAME_FIELD = "email"

#      REQUIRED_FIELDS = ['username']

#      def _str_(self):
#           return self.username