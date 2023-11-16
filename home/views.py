from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def product(request):
    return render(request,'product.html')

def logpage(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')