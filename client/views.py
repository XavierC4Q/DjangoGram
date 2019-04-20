from django.shortcuts import render
import requests

def index(request):
    get_users = requests.get('http://localhost:8000/api/user/')
    users = get_users.json()
    context = {
        'users': users
    }

    return render(request, 'client/index.html', context)
