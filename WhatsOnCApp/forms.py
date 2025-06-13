from django import forms
from django.forms import fields, ModelForm
from .models import Provider, Image

class ProviderForm(forms.ModelForm):
    
    class Meta:
        model= Provider
        fields=('name', 'phone', 'email', 'location', 'vcode',)

class ProviderImgForm(forms.ModelForm):

    class Meta:
        model=Image
        fields=('image', 'caption')