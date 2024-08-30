from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

# from ad.forms import SellerForm
from ad.models import Seller



def indexxx(request):
    return render(request,"indexxx.html") 



def seller(request):
    # if request.method == 'POST':
    #     form = SellerForm(request.POST)
    #     if form.is_valid():
    #         seller = form.save()
    #         messages.success(request, 'Seller added successfully.')
    #         return redirect('seller_management')
    # else:
    #     form = SellerForm()

    sellers = Seller.objects.all()
    return render(request, 'manageseller.html', {'sellers': sellers})