from django.urls import path
from . import views

app_name="WhatsOnCApp"

urlpatterns=[path('', views.home, name="home"),
             path('calendar/', views.listView, name="calendar"),
             path('event/', views.detailView, name="event"),
             path('providerRegistration/', views.providerForm, name="providerRegistration"),
             path('success/', views.success, name="sucess"),
             path('contactUs/', views.contactUsForm, name="contactUs"),
]