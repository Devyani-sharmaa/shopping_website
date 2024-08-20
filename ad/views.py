from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render



def indexxx(request):
    return render(request,"indexxx.html") 