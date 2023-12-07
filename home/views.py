from django.shortcuts import render,redirect
from .models import Slider
from .models import Category
from .models import Product
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

# Create your views her
def index(request):
    banner = Slider.objects.all()
    dict ={
        'banners':banner
    }
    return render(request,'index.html',dict)

def collections(request):
    category = Category.objects.filter(status=0)
    banner = Slider.objects.all()
    dict1 ={
        'banners':banner,
        'category':category,
    }

    return render(request,'collections.html',dict1)

def logpage(request):
    banner = Slider.objects.all()
    dict ={
        'banners':banner
    }
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            
            auth.login(request, user)
            return redirect('/')
        else:
          
            messages.info(request, "Invalid Login")
            return redirect('/login')
            

    return render(request,'login.html',dict)

def register(request):
    banner = Slider.objects.all()
    dict = {'banners': banner}

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            return redirect('register')

        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            # Redirect after successful registration
            return redirect('/')
        else:
            messages.error(request, 'Passwords do not match. Please try again')
            return render(request, 'register.html', dict)

    return render(request, 'register.html', dict)

        
    

def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug,status = 0)):

        product = Product.objects.filter(category__slug = slug)
         
    else:
        messages.error(request, "Category not found")
        return redirect('collcetions')
    return render(request,'product.html',{"product":product}) 

def product(request):
    product = Product.objects.filter(status=0)
    banner = Slider.objects.all()
    dict1 ={
        'banners':banner,
        'product':product,
    }
    
    return render(request,'product.html',dict)

def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug,status = 0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            bd = Product.objects.filter(slug=prod_slug,status=0)
        
        else:
             messages.error(request, "No such product found")
             return redirect('collections')
    else:
        messages.error(request,'no such category found')
        return redirect('collections')

def logout(request):
    auth.logout(request)
    return redirect('/')

    

