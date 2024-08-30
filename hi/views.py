from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from ds.models import add_product
from ds.models import Order


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from hi.models import UserCheck
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def index(request):
    user = User.objects.get(username = request.user)
    check_seller = UserCheck.objects.filter(userx = user).last()
    print(check_seller, "xxxxxxxxxxx")
    if check_seller:
        if check_seller.is_seller:
                return render(request, "home.html")
        else:
                return HttpResponse("your are not authorize....")
    else:
            return HttpResponse("your are not authorize....")
    return render(request,"index.html") 


@login_required(login_url="/login")
def productsidebar(request):
    y=add_product.objects.all()
    return render(request,"product-sidebar.html",{"my_data":y})

def productinfo(request):
    return render(request,"product-info.html")


def about(request):
    return render(request,"about.html")


def cart(request):
    z=Order.objects.all()
    return render(request,"cart.html",{"my_dataa":z})


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



def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passwrd = request.POST.get("pass")

        checkuser = authenticate(username = username, password = passwrd)

        if checkuser is not None:
            login(request, checkuser)
            return redirect("/hi/index")


    return render(request, "loginpage.html")

def signuppage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        email = request.POST.get("email")
        passsword = request.POST.get("pass")

        newuser = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = passsword)
        newuser.save()

        checkdata = UserCheck(userx = newuser, is_seller = True)
        checkdata.save()

    return render(request, "signuppage.html")



def logutnow(request):
    logout(request)
    return redirect("/hi/index")