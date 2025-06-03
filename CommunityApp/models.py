from django.db import models
from django.contrib.auth.models import User
from WhatsOnCApp.models import Event

# Create your models here.

class Role(models.Model):
    
    type=models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.type

class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role= models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
class Bookmarks(models.Model):

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_bookmark', null=False, blank=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False, blank=False)
    # if get to implement a note to the bookmark
    tag = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user