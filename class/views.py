from django.shortcuts import render
from .models import Room
from .forms import RoomForm

def home(request ):
    rooms = Room.objects.all()
    context={'rooms':rooms}
    return render(request, 'class/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
        
    context = {'room': room}
    return render(request, 'class/room.html', context)

def createRoom(request):
    room=RoomForm()
    context={room:room}
    return render(request, 'class/room_form.html', context)