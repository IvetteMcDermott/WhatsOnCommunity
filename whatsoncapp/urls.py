from django.urls import path
from . import views

app_name="whatsoncapp"

urlpatterns=[path('', views.home, name="home"),
            path('controlPanel/', views.controlPanel, name="controlPanel"),
            path('events/json/', views.eventListJson, name='eventListJson'),
            path('calendar/', views.calendarView, name="calendar"),
            path('event/<int:id>/', views.detailView, name="event"),
            path('editEvent/<int:id>/', views.editEvent, name="editEvent"),
            path('providerRegistration/', views.providerForm, name="providerRegistration"),
            path('eventPost/', views.eventForm, name="eventPost"),
            path('success/', views.success, name="success"),
            path('approveProv/<int:id>/', views.ApproveProv, name="approveProv"),
            path('deleteProvApplication/<int:id>/', views.deleteProvApplication, name="deleteProvApplication"),
            path('deleteEventApplication/<int:id>/', views.deleteEventApplication, name="deleteEventApplication"),
            path('approveEv/<int:id>/', views.ApproveEv, name="approveEv"),
            path('messageCU/<int:id>/', views.messageContactUs, name="messageCU"),
            path('contactUs/', views.contactUsForm, name="contactUs"),
            path('solvedCU/<int:id>/', views.solvedContactUs, name='solvedCU'),
]