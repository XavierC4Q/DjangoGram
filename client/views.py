from django.shortcuts import render
import requests as req

def index(request):

    return render(request, 'client/home.html')


def user_detail_view(request, pk=None):
    get_single_user = req.get(f'http://localhost:8000/api/user/{pk}')

    if get_single_user.status_code == 404:
        return render(request, 'client/notfound.html')

    single_user = get_single_user.json()
    context = {
        'user': single_user
    }

    return render(request, 'client/detail.html', context)