from django.db import models

# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to="sliderfield")
    sale = models.IntegerField()
    text_para = models.TextField(max_length=250)
    link = models.CharField(max_length=100,default="")

    def __str__(self) -> str:
        return self.text_para
    