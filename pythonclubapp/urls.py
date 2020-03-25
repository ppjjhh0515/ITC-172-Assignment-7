from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getresources/', views.getresources, name='types'),
    path('getmeetings/', views.getmeetings, name='meeting'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='meetingid'),
]