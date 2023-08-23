from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
path('class/room/<str:pk>/', views.room, name='room')
]