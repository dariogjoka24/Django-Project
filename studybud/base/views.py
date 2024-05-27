from typing import Optional
from xml.dom import NotFoundErr
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render 
from base.models import User

rooms: list[dict] = [
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Learn C#'},
    {'id': 3, 'name': 'Learn Java'}
]

def home(request: HttpRequest) -> HttpResponse:
    context = {}
    try:
        users = User.objects.all()
        if users:
            print("Users retrieved successfully from database!")
            for user in users:
                admin = False
                if user.full_name == "Dario Gjoka":
                    admin = True
                context[user.full_name + "admin" if admin else user.full_name] = user.email
        else:
            print("Users could not be retrieved from database") 
    except NotFoundErr as e:
        print(e)
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request: HttpRequest, pk: str) -> HttpResponse:
    room: Optional[dict] = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r
            break
    context = { 'room': room }
    return render(request, 'base/room.html', context)
