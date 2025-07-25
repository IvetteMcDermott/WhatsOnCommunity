from django import forms
from django.forms import fields, ModelForm
from .models import Provider, Image, Event, ImageEvent, Category, ContactUs

class ProviderForm(forms.ModelForm):
    
    class Meta:
        model= Provider
        exclude=['approved', 'user']
class ProviderImgForm(forms.ModelForm):

    class Meta:
        model=Image
        fields=('image', 'caption')

class EventForm(forms.ModelForm):

    class Meta:
        model= Event
        exclude=['approved', 'provider']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['startDate'].widget = forms.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control',
            }
        )
        self.fields['startTime'].widget = forms.TimeInput(
            attrs={
                'type': 'time',  
                'class': 'form-control',
            }
        )
        self.fields['endDate'].widget = forms.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control',
            }
        )
        self.fields['endTime'].widget = forms.TimeInput(
            attrs={
                'type': 'time',  
                'class': 'form-control',
            }
        )


class EditEventForm(forms.ModelForm):

    class Meta:
        model= Event
        exclude=['category', 'title', 'approved', 'provider']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['startDate'].widget = forms.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control',
            }
        )
        self.fields['startTime'].widget = forms.TimeInput(
            attrs={
                'type': 'time',  
                'class': 'form-control',
            }
        )
        self.fields['endDate'].widget = forms.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control',
            }
        )
        self.fields['endTime'].widget = forms.TimeInput(
            attrs={
                'type': 'time',  
                'class': 'form-control',
            }
        )

class EventImgForm(forms.ModelForm):

    class Meta:
        model=ImageEvent
        fields=('image', 'caption')

class CategoryForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a category")


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        exclude=['sent_at', 'solved']

class SolvedCU(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields=('solved',)


class ApproveProv(forms.ModelForm):

    class Meta:
        model = Provider
        fields=('approved',)

class ApproveEv(forms.ModelForm):

    class Meta:
        model = Event
        fields=('approved',)