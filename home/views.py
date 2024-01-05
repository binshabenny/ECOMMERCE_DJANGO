from django.shortcuts import render,redirect,get_object_or_404
from .models import Slider
from .models import Category
from .models import Product
from .models import ProductDetailView,CartItem,Cart
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views her
def index(request):
    banner = Slider.objects.all()
    dict ={
        'banners':banner
    }
    return render(request,'index.html',dict)

@login_required(login_url='login')
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
    
    return render(request,'product.html',dict1)

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
    

def detail_view(request, prod_slug):
        
        product = get_object_or_404(Product, slug=prod_slug, status=0)
        product_details = ProductDetailView.objects.filter(product=product)

        if request.method == "POST":
            messages.success(request, f"{product.name} added to your cart.")
            return redirect("add_to_cart", product_id=product.id)
            
        context = {
            'product': product,
            'product_details': product_details,
            }

        return render(request, 'detail_view.html', context)




def view_cart(request):

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        return render(request, 'view_cart.html', {'cart_items': cart_items})
    return redirect('login')  # Redirect to login page if user is not authenticated
@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.product.selling_price for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "cart/cart_detail.html", context)

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    print(f"User: {request.user}")
    print(f"Cart Items: {cart_items}")
    
    # Initialize total_price for all cart items
    total_price = 0

    # List to store details of each cart item
    cart_details = []

    for item in cart_items:
        # Calculate the total price for each cart item
        item_total_price = item.quantity * item.product.selling_price

        # Add the individual product price to the total_price
        total_price += item_total_price

        # Apply discount
        discount = 60.00
        discounted_total_price = max(0, total_price - discount)

        # Apply tax
        tax = 14.00
        total_with_tax = discounted_total_price + tax

        # Append cart item details to the list
        cart_details.append({
            'product_id': item.product.id,
            'cart_item_id': item.id,
            'product_name': item.product.name,
            'selling_price':item.product.selling_price,
            'product_img':item.product.product_image,
            'quantity': item.quantity,
            'price_per_piece': item.product.selling_price,
            'total_price': item_total_price,
            "discounted_total_price": discounted_total_price,
            "tax": tax,
            "discount":discount,
            "total_with_tax": total_with_tax,
        })

    context = {
        'cart_details': cart_details,
        'total_price': total_price,
    }

    return render(request, "cart.html", context)


@login_required
def add_to_cart(request, product_id):
    # Get the Product instance using the provided product_id
    product = get_object_or_404(Product, id=product_id)

    # Check if the user already has this product in the cart
    cart_item = Cart.objects.filter(user=request.user, product=product).first()

    if cart_item:
        # If the product is already in the cart, increase the quantity
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to your cart.")
    else:
        # If the product is not in the cart, create a new cart item
        Cart.objects.create(user=request.user, product=product, quantity=1)
        messages.success(request, "Item added to your cart.")

    return redirect("cart")

@login_required
def remove_from_cart(request, product_id):
    # Get the Product instance using the provided product_id
    product = get_object_or_404(Product, id=product_id)
    

    cart_item = Cart.objects.filter(user=request.user, product=product).first()

    # If a cart item is found, decrement the quantity by 1
    if cart_item:
        cart_item.quantity -= 1

        # If the quantity becomes zero, remove the cart item
        if cart_item.quantity <= 0:
            cart_item.delete()
            messages.success(request, "Item removed from your cart.")
        else:
            cart_item.save()
            messages.success(request, "Quantity updated in your cart.")

    return redirect("cart")

@login_required
def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item.quantity = quantity
        cart_item.save()
        # You may want to redirect to the cart page or return a JSON response
        # with the updated total price and any other necessary information.
    return redirect('cart')  # Update with your cart page URL





def logout(request):
    auth.logout(request)
    return redirect('/')

    
def contact(request):
    return render(request,'contact.html')

def test(request):
    return render(request,'test.html')