from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def userProfile(request):
    return render(request, 'userProfile.html')

def providerProfile(request):
    return render(request, 'providerProfile.html')
