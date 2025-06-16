from django.shortcuts import render, redirect
from .forms import ProviderForm,ProviderImgForm, EventForm, EventImgForm
from django.contrib.auth.models import User

from .models import Provider


# Create your views here.
def home(request):
    return render(request, 'index.html')

def listView(request):
    return render(request, 'listView.html')

def detailView(request):
    return render(request, 'detailView.html')

def providerForm(request):
    if request.method == 'POST':
        formP= ProviderForm(request.POST)
        formI= ProviderImgForm(request.POST, request.FILES)

        if formP.is_valid() and formI.is_valid():
            provider=formP.save(commit=False)
            user=request.user
            provider.user=user
            provider=formP.save()
            image=formI.save(commit=False)
            image.provider=provider
            image.save()
            return render(request,'success.html')
    else:
        formP=ProviderForm()
        formI=ProviderImgForm()
    return render(request, 'providerForm.html', {'formP':formP, 'formI': formI })

def eventForm(request):
    if request.method == 'POST':
        formE= EventForm(request.POST)
        formIE= EventImgForm(request.POST, request.FILES)
        if formE.is_valid() and formIE.is_valid():
            event=formE.save(commit=False)
            provider = Provider.objects.get(user=request.user)
            event.provider=provider
            event=formE.save()
            imageEvent=formIE.save(commit=False)
            imageEvent.event=event
            imageEvent.save()
            return render(request, 'success.html')
    else:
        formE= EventForm()
        formIE= EventImgForm()
        return render(request, 'eventsForm.html', {'formE':formE, 'formIE':formIE})


def success(request):
    return render(request, 'success.html')

def contactUsForm(request):
    return render(request, 'contactUs.html')
