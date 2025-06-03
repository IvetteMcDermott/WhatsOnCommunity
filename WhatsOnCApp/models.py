from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural='Categories'
    
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Provider(models.Model):

    name=models.CharField(max_length=100, blank=False, null=False)
    phone=models.IntegerField(blank=False, null=False)
    email=models.EmailField(null=False, blank=False)
    location=models.CharField(max_length=200, null=False, blank=False)
    vcode=models.CharField(max_length=10, null=False, blank=False)

class Image(models.Model):
    image=CloudinaryField(max_length=255, verbose_name='image' )
    caption=models.CharField(max_length=200, null=False, blank=False)

class Event(models.Model):

    category=models.ForeignKey(Category, on_delete=models.CASCADE, default='Category')
    title=models.CharField(max_length=200, null=False, blank=False)
    date=models.DateField(null=False, blank=False)
    time=models.TimeField(null=False, blank=False)
    location=models.CharField(max_length=200, null=False, blank=False)
    vcode=models.CharField(max_length=10,null=False, blank=False)
    provider=models.ForeignKey(Provider, on_delete=models.CASCADE, default='Provider')
    
