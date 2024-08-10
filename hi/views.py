from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from ds.models import add_product




def index(request):
    return render(request,"index.html") 


def productsidebar(request):
    y=add_product.objects.all()
    return render(request,"product-sidebar.html",{"my_data":y})

def productinfo(request):
    return render(request,"product-info.html")


def about(request):
    return render(request,"about.html")


def cart(request):
    return render(request,"cart.html")


def index(request):
    return render(request,"index.html")


def user_profile(request):
    return render(request,'user-profile.html')

def become_vendor(request):
    return render(request,"become-vendor.html")


def checkout(request):
    return render(request,"checkout.html")



def compaire(request):
    return render(request,"compaire.html")


def contact_us(request):
    return render(request,"contact-us.html")

def add_to_cart(request):
    return render(request,"cart.html")


def create_account(request):
    return render(request,"create-account.html")


def order(request):
    return render(request,"order.html")


def faq(request):
    return render(request,"faq.html")