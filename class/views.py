from django.shortcuts import render

# Create your views here.
rooms = [
    {'id': 1, 'name': '101', 'floor': 1, 'beds': 2},
    {'id': 2, 'name': '201', 'floor': 2, 'beds': 1},
    {'id': 3, 'name': '301', 'floor': 3, 'beds': 3},
]

def home(request ):
    context={'rooms':rooms}
    return render(request, 'class/home.html', context)

def room(request, pk):
    return render(request,'class/room.html')