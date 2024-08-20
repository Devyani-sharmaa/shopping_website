from django.contrib import admin
from ds.models import add_product
from ds.models import Order
# from ds.models import User
# Register your models here.


admin.site.register(add_product)
admin.site.register(Order)

# admin.site.register(User)