from django.contrib import admin
from .models import Provider, Image, Category,  Event, ImageEvent

admin.site.register(Provider)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(ImageEvent)