from django.urls import path
from . import views

app_name="CommunityApp"

urlpatterns=[path('userProfile/', views.userProfile, name="userProfile"),
             path('providerProfile/', views.providerProfile, name="providerProfile"),
             path('bookmark/<int:id>', views.bookmarking, name='bookmark')
]