# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })

def phone(request):
    return render(request, 'draw/phone.html')

def shared(request):
    return render(request, 'draw/shared.html')

def submitted(request):
    return render(request, 'draw/submitted.html')

def phone2(request):
    return render(request, 'draw/phone2.html')

def shared2(request):
    return render(request, 'draw/shared2.html')
