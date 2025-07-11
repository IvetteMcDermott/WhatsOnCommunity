from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import UserProfile, Bookmarks
from WhatsOnCApp.models import Event, Provider
from django.contrib.auth.models import User


from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def userProfile(request):

    user = get_object_or_404(UserProfile, user=request.user)
    bookmarks = Bookmarks.objects.filter(user=user)

    return render(request, 'userProfile.html', {'userP': user,
'bookmarks': bookmarks})

def providerProfile(request, id):

    provider=get_object_or_404(Provider, id=id)
    provider_imgs=provider.provider_img.all()
    return render(request, 'providerProfile.html', {'provider':provider, 'provider_imgs': provider_imgs})

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
