from django.db import models

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
    

