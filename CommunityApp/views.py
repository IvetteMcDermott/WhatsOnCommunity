from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import UserProfile, Bookmarks
from WhatsOnCApp.models import Event
from django.contrib.auth.models import User


from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def userProfile(request):

    return render(request, 'userProfile.html')

def providerProfile(request):
    return render(request, 'providerProfile.html')

@login_required
def bookmarking(request, id):
    if request.method=='POST':
        user = UserProfile.objects.get(user=request.user)
        event=get_object_or_404(Event, id=id)
        bookmark_event, created = Bookmarks.objects.get_or_create(user=user, event=event)
             
        if created:
            # If created, bookmark didn't exist
            print("Bookmark added.")
        else:
            # If existed, delete it
            bookmark_event.delete()
            print("Bookmark removed.")


    return HttpResponseRedirect(request.META['HTTP_REFERER'])
