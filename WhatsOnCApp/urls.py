from django.urls import path
from . import views

app_name="WhatsOnCApp"

urlpatterns=[path('', views.home, name="home"),
             path('events/json/', views.eventListJson, name='eventListJson'),
             path('calendar/', views.calendarView, name="calendar"),
             path('event/<int:id>/', views.detailView, name="event"),
             path('providerRegistration/', views.providerForm, name="providerRegistration"),
             path('eventPost/', views.eventForm, name="eventPost"),
             path('success/', views.success, name="success"),
             path('contactUs/', views.contactUsForm, name="contactUs"),
]