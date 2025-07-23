from django.db import models
from django.contrib.auth.models import User
from whatsoncapp.models import Event

# Create your models here.

class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
   
    
    def __str__(self):
        return str(self.name)
    
class Bookmarks(models.Model):

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_bookmark', null=False, blank=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False, blank=False)
    # if get to implement a note to the bookmark
    tag = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user