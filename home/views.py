from django.shortcuts import render
from .models import Slider
# Create your views here.
def index(request):
    banner = Slider.objects.all()
    dict ={
        'banners':banner
    }
    return render(request,'index.html',dict)

def product(request):
    banner = Slider.objects.all()
    dict ={
        'banners':banner
    }
    return render(request,'product.html',dict)

def logpage(request):
    banner = Slider.objects.all()
    dict ={
        'banners':banner
    }
    return render(request,'login.html',dict)

def register(request):
    banner = Slider.objects.all()
    dict ={
        'banners':banner
    }
    return render(request,'register.html',dict)