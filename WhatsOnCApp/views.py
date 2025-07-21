from django.shortcuts import render, redirect, get_object_or_404
from datetime import timedelta, datetime
from django.db.models import Q

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from CommunityApp.models import Bookmarks, UserProfile

from .forms import ProviderForm,ProviderImgForm, EventForm, EventImgForm, CategoryForm, ContactUsForm, SolvedCU, EditEventForm
from django.contrib.auth.models import User

from .models import Provider, Event, Category, ContactUs


# Create your views here.
def home(request):
    return render(request, 'index.html')

# fetch the data and convert it to Json format
def eventListJson(request):
    # all approved events
    events = Event.objects.filter(approved=True)

    data = []

    # get the category value if the form is submitted. empty is by default 
    categoryF=request.GET.get('category', '')
    # render the events according to the category selected, if empty will render all 
    if categoryF=="all" or categoryF == "":
        events = Event.objects.filter(approved=True)
    else:
        events=events.filter(Q(category=categoryF))

    # Jsonfy the events for the calendar
    for event in events:
        current_day = event.startDate
        while current_day <= event.endDate:
            start_datetime = f"{current_day}T{event.startTime}"
            end_datetime=f"{current_day}T{event.endTime}"
            data.append({
                "id":event.id,
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

# calendar
def calendarView(request):
    categories = Category.objects.all() 
    formcat=CategoryForm()
    return render(request, 'calendarView.html', {'formcat':formcat, 'categories': categories})

def detailView(request, id, *args, **kwargs):
    event=get_object_or_404(Event, id=id)
    event_images = event.event_img.all()
    bookmarked=False
    
    if request.user.is_authenticated:
        if not request.user.is_staff:
            user = UserProfile.objects.get(user=request.user)
            bookmarke = Bookmarks.objects.filter(
            user=user, event=event).exists()

            if bookmarke:
                bookmarked = True
                messages.success(request, 'You had bookmarked the event successfully!')
            else:
                bookmarked = False
                messages.success(request, 'Your bookmarked had been removed!')
    
    return render(request, 'detailView.html',{'event':event,'event_images': event_images, 'id':id, 'bookmarked':bookmarked})

def editEvent(request, id):
    event = get_object_or_404(Event, id=id)
    form=EditEventForm()
    if request.method=='POST':
        form=EditEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            messages.success(request,'Your event had been edited successfully!')
            return redirect ('/calendar/')
        
        form = EditEventForm(instance=event)
    return render(request, 'eventsForm.html',{"form":form, "event":event})

# form to register as provider that requires the user has an account
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
            messages.success(request,'Your application had been sent successfully!')
            return render(request,'success.html')
    else:
        formP=ProviderForm()
        formI=ProviderImgForm()
        messages.error(request,'Your application needs to be review!')

    return render(request, 'providerForm.html', {'formP':formP, 'formI': formI })

# form to submit an event
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
            messages.success(request,'Your event had been sent successfully!')
            return render(request, 'success.html')
    else:
        formE= EventForm()
        formIE= EventImgForm()
        return render(request, 'eventsForm.html', {'formE':formE, 'formIE':formIE})

# success page after successful submission
def success(request):
    return render(request, 'success.html')

# form to contact the staff
def contactUsForm(request):
    formCU = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            messages.success(request,'Your enquiry had been sent successfully!')
            formCU = ContactUsForm()
            return redirect('WhatsOnCApp:home')
        else:
            form = ContactUsForm()
            return render(request, 'contactUs.html', {'formCU': formCU})

    return render(request, 'contactUs.html', {'formCU': formCU})

def messageContactUs(request, id):
    message=get_object_or_404(ContactUs, id=id)

    return render(request, "messageContactUs.html",{'message': message})


# ADMIN

@staff_member_required
def solvedContactUs(request, id):
    
    message=get_object_or_404(ContactUs, id=id)
       
    if request.method=='POST':
        if 'solved' in request.POST:
            message.solved=True
            message.save()
            messages.success(request,'Marked solved successfully!')

        else:
            message.solved=False
    return redirect('WhatsOnCApp:controlPanel') 

@staff_member_required
def ApproveProv(request, id):
    
    provider=get_object_or_404(Provider, id=id)
       
    if request.method=='POST':
        if 'approved' in request.POST:
            provider.approved=True
            provider.save()
            messages.success(request,'Provider approved successfully!')
        else:
            provider.approved=False
    return redirect('WhatsOnCApp:controlPanel') 

@staff_member_required
def ApproveEv(request, id):
    
    event=get_object_or_404(Event, id=id)
       
    if request.method=='POST':
        if 'approved' in request.POST:
            event.approved=True
            event.save()
            messages.success(request,'Event approved successfully!')
        else:
            event.approved=False
    return redirect('WhatsOnCApp:controlPanel') 

def deleteProvApplication(request, id):

    if request.method=='GET':
        provider=get_object_or_404(Provider, id=id)
        provider.delete()
        messages.success(request,'Provider application deleted!')
    return redirect('WhatsOnCApp:controlPanel') 

def deleteEventApplication(request, id):

    if request.method=='GET':
        event= get_object_or_404(Event, id=id)
        event.delete()
        messages.success(request,'Event application deleted!')
    return redirect('WhatsOnCApp:controlPanel') 

@staff_member_required
def controlPanel(request):
    providersApps=Provider.objects.filter(approved=0)
    eventsApps=Event.objects.filter(approved=0)
    messagesIn=ContactUs.objects.filter(solved=False)
    return render(request, "controlPanel.html", {'providersApps': providersApps, 'eventsApps': eventsApps, 'messagesIn':messagesIn})