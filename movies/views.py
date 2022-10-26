from django.http import HttpResponse
from django.shortcuts import render


data = {
    'movies':
    [
        {
            'id': 5,
            'title': 'Jaws',
            'year': '1669',
        },
        {
            'id': 6,
            'title': 'James Bond',
            'year': '1956',
        },
        {
            'id': 7,
            'title': 'Moonraker',
            'year': '1823',
        },
    ]
}


def movies(request):
    return render(request, 'movies/movies.html', data)


def home(request):
    return HttpResponse("Home page")
