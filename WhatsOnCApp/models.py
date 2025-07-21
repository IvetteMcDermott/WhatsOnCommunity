from django.contrib.auth.models import User

from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):
  
    class Meta:
        verbose_name_plural='Categories'
    
    name=models.CharField(max_length=15,unique=True)

    def __str__(self):
        return self.name

class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name=models.CharField(max_length=100, blank=False, null=False)
    phone=models.IntegerField(blank=False, null=False)
    email=models.EmailField(null=False, blank=False)
    location=models.CharField(max_length=200, null=False, blank=False)
    vcode=models.CharField(max_length=10, null=False, blank=False)
    description=models.TextField(max_length=500, null=False, blank=True)
    approved=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Image(models.Model):
    provider= models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="provider_img")
    image=CloudinaryField(max_length=255, verbose_name='image' )
    caption=models.CharField(max_length=200, null=False, blank=False)

class Event(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=200, null=False, blank=False)
    startDate=models.DateField(null=False, blank=False)
    startTime=models.TimeField(null=False, blank=False)
    endDate=models.DateField(null=False, blank=False)
    endTime=models.TimeField(null=False, blank=False)
    location=models.CharField(max_length=200, null=False, blank=False)
    vcode=models.CharField(max_length=10,null=False, blank=False)
    description=models.TextField(max_length=800, null=False, blank=True)
    provider=models.ForeignKey(Provider, on_delete=models.CASCADE)
    approved=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class ImageEvent(models.Model):
    event= models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_img")
    image=CloudinaryField(max_length=255, verbose_name='imageE' )
    caption=models.CharField(max_length=200, null=False, blank=False)

class ContactUs(models.Model):
    subject = [
              ('provider', 'About a provider'),
              ('event', 'About an event'),
              ('enquiry', 'General enquiry'),
              ('claim or complain', 'Claim or Complain'),
    ]
     
    name=models.CharField(max_length=200, null=False, blank=False)
    email=models.EmailField(null=False, blank=False)
    subject=models.CharField(max_length=30, choices=subject, null=False, blank=False)
    description=models.TextField(max_length=800, null=False, blank=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    solved=models.BooleanField(default=False)

    def __str__(self):
        return f'Message {self.subject} by {self.email} on {self.sent_at}'
