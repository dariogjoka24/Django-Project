from typing import Optional
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render 

rooms: list[dict] = [
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Learn C#'},
    {'id': 3, 'name': 'Learn Java'}
]

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'base/home.html', {'rooms': rooms})
    

def room(request: HttpRequest, pk: str) -> HttpResponse:
    room: Optional[dict] = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r
            break
    context = { 'room': room }
    return render(request, 'base/room.html', context)
