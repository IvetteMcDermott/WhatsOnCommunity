from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')

def listView(request):
    return render(request, 'listView.html')

def detailView(request):
    return render(request, 'detailView.html')

def providerForm(request):
    return render(request, 'formRegisterProvider.html')

def success(request):
    return render(request, 'success.html')

def contactUsForm(request):
    return render(request, 'contactUs.html')
