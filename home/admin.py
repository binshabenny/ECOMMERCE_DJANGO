from django.contrib import admin
from .models import Slider  
from .models import Category,Product,ProductDetailView
# Import your model


# Register your models here.

admin.site.register(Slider) 
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductDetailView)


