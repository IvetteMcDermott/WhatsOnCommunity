from django.shortcuts import render, redirect
from .forms import ProviderForm,ProviderImgForm


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
            provider=formP.save()
            image=formI.save(commit=False)
            image.provider=provider
            image.save()
            return render(request,'success.html')
    else:
        formP=ProviderForm()
        formI=ProviderImgForm()
    return render(request, 'providerForm.html', {'formP':formP, 'formI': formI })

def success(request):
    return render(request, 'success.html')

def contactUsForm(request):
    return render(request, 'contactUs.html')
