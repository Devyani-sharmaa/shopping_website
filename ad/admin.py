from django.contrib import admin
from django import forms
from ad.models import Seller


class SellerAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'email', 'contact_number')
    search_fields = ('store_name', 'email')

admin.site.register(Seller, SellerAdmin)


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('store_name', 'address', 'contact_number', 'email')