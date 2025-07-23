from django.urls import path
from . import views

app_name="communityapp"

urlpatterns=[path('userProfile/', views.userProfile, name="userProfile"),
             path('providerProfile/<int:id>', views.providerProfile, name="providerProfile"),
             path('bookmark/<int:id>', views.bookmarking, name='bookmark')
]