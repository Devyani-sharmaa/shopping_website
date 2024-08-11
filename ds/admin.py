from django.contrib import admin
from ds.models import add_product
from ds.models import Order
# Register your models here.


admin.site.register(add_product)
admin.site.register(Order)