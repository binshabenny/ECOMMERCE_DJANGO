from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to="sliderfield")
    sale = models.IntegerField()
    text_para = models.TextField(max_length=250)
    link = models.CharField(max_length=100,default="")

    def __str__(self) -> str:
        return self.text_para


class Category(models.Model):
    slug = models.CharField(max_length=50, null = False, blank = False)
    name =  models.CharField(max_length=100,null=False,blank = False)
    image = models.ImageField(upload_to="category_img",null =False,blank=False)
    status = models.IntegerField(default=False,help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False,help_text="0=default, 1=hidden")

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=50, null = False, blank = False)
    name = models.CharField(max_length=100,null=False,blank = False)
    product_image =models.ImageField(upload_to="category_img",null =False,blank=False)
    description = models.CharField(max_length=500,null=False,blank = False)
    quantity = models.IntegerField(null=False,blank=False)
    original_price =models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    status = models.IntegerField(default=False,help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False,help_text="0=default, 1=hidden")

    def __str__(self):
        return self.name
    
class ProductDetailView(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE, null=False, blank=False)
    pdt_colour = models.CharField(max_length=100,null=False,blank = False)
    pdt_description = models.TextField(max_length=250,null=False,blank = False)
    pdt_image1 = models.ImageField(upload_to="detail_img",null =False,blank=False)

    def __str__(self):
        return f"{self.product.name} - {self.pdt_colour}"

    def get_product_image(self):
        return self.product.product_image
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    def total_price(self):
        return self.product.selling_price * self.quantity

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    def get_absolute_url(self):
        return reverse("cart")



    

