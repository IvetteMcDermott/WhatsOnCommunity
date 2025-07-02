from django.shortcuts import render, redirect
from datetime import timedelta, datetime

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


from .forms import ProviderForm,ProviderImgForm, EventForm, EventImgForm
from django.contrib.auth.models import User

from .models import Provider, Event


# Create your views here.
def home(request):
    return render(request, 'index.html')


def eventListJson(request):
    events = Event.objects.filter(approved=True)
    data = []

    for event in events:
        current_day = event.startDate
        while current_day <= event.endDate:
            start_datetime = f"{current_day}T{event.startTime}"
            end_datetime=f"{current_day}T{event.endTime}"
            data.append({
                "category": event.category.name,
                "title": event.title,
                "start": start_datetime, 
                "end": end_datetime,
                "when": current_day,
                "time": event.startTime,
                "endDate": current_day,
                "endTime": event.endTime,
                "location": event.location,
                "vcode": event.vcode,
                "description": event.description,
                "provider": event.provider.name,
            })

            current_day += timedelta(days=1)

    return JsonResponse(data, safe=False)

def listView(request):
    return render(request, 'listView.html')

def detailView(request):
    return render(request, 'detailView.html')

@login_required
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

@login_required 
def eventForm(request):
    # Security in case unauthorized user access to the form, it would redirect them 
    # to the provider registration form
    is_provider=Provider.objects.filter(user=request.user).exists()

    if not is_provider:
        # message('You are not a register provider')
        return redirect("/providerRegistration/")
    # end of verification

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

# admin