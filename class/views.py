from django.shortcuts import render
from .models import Room
 
# Create your views here.
# rooms = [
#     {'id': 1, 'name': 'East Wing', 'floor': 1, 'beds': 2},
#     {'id': 2, 'name': 'Southwest wing', 'floor': 2, 'beds': 1},
#     {'id': 3, 'name': 'North-Eastern Wing', 'floor': 3, 'beds': 3},
# ]

def home(request ):
    rooms = Room.objects.all()
    context={'rooms':rooms}
    return render(request, 'class/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
        
    context = {'room': room}
    return render(request, 'class/room.html', context)
