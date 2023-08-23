from django.shortcuts import render

# Create your views here.
rooms = [
    {'id': 1, 'name': '101', 'floor': 1, 'beds': 2},
    {'id': 2, 'name': '201', 'floor': 2, 'beds': 1},
    {'id': 3, 'name': '301', 'floor': 3, 'beds': 3},
]

def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request,'room.html')