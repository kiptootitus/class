from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('class/room/<int:pk>/', views.room_view, name='room')
]