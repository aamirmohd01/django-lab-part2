from django.shortcuts import render
from django.http import HttpResponse

def track_visits(request):
    if 'visits' in request.COOKIES:
        visits = int(request.COOKIES['visits']) + 1
    else:
        visits = 1

    response = HttpResponse(f"Number of visits: {visits}")
    response.set_cookie('visits', visits)
    return response
