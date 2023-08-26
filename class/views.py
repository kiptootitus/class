from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RoomForm

def loginPage(request):
    page = 'login'
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or Password is incorrect')

    context={}
    return render(request, 'class/login.html', context)
def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = UserCreationForm()
    
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
        
    return render('request', 'class/login.html', {'form':form})
        
    
    
    
def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q)
        |Q(name__icontains=q)|
        Q(description__icontains=q)
    )    
    topics = Topic.objects.all()
    room_count = rooms.count()

    context={'rooms':rooms, 'topics':topics, 'room_count':room_count}
    return render(request, 'class/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
        
    context = {'room': room}
    return render(request, 'class/room.html', context)

@login_required(login_url='login')
def createRoom(request):
    form=RoomForm()
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'class/room_form.html', context)

def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    if request.method=='POST':
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('/')
    if request.user != room.host:
        return HttpResponse('You are not allowed here') 
    context={'form':form}
    return render(request, 'class/room_form.html', context)

def deleteRoom(request):
    pass
