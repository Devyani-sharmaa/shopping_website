from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from ds.models import Order



def indexx(request):
    return render(request,"indexx.html") 

def mailbox(request):
    return render(request,"mailbox.html")

def chart(request):
    return render(request,"chart.html")


def basic_table(request):
    return render(request,"basic-table.html")


def data_table(request):
    return render(request,"data-table.html")


def layouts(request):
    return render(request,"layouts.html")

def login(request):
    return render(request,"login.html")


def forget_password(request):
    return render(request,"forget-password")


def add_product(request):
    return render(request,"add_product.html")

def saveproduct(request):
    if request.method=="POST":
        product_name=request.POST.get("pname")
        price_description=request.POST.get("pdes")
        price=request.POST.get("price")
        old_price=request.POST.get("oprice")
        rating=request.POST.get("rate")
        out_of=request.POST.get("orate")
        image1=request.POST.get("img1")
        # image2=request.POST.get("img2")
        # image3=request.POST.get("img3")
        price=request.POST.get("price")
        data=add_product(product_name=product_name,price_description=price_description,price=price, old_price=old_price, rating=rating ,out_of=out_of,image1=image1,image2=image2,image3=image3)
    data.save()
    return redirect('add_product.html')



def deletefata(request, x):
    q = add_product.objects.get(id = x)
    q.delete()
    return redirect('add_product.html')


     
def order_detail(request):
    # if request.method=="POST":
    #     product=request.Post.get("Product")
    #     price=request.Post.et("price")
    #     quantity=request.Post.get("quantity")
    #     order_date=request.Post.get("order_date")
    #     status=request.Post.get("status")

    #     dt=order_detail(product=product,price=price,quantity=quantity,order_date=order_date,status=status)
    # dt.save()

    z=Order.objects.all()
    return render(request,"orderdetails.html",{"my_dataa":z}) 