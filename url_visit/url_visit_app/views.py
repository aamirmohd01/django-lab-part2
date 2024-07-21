from django.shortcuts import render
from django.http import HttpResponse

def track_visits(request):
    visit_count = request.COOKIES.get('visit_count', 0)
    visit_count = int(visit_count) + 1

    response = HttpResponse(f'This page has been visited {visit_count} times.')

    # Set the cookie with the updated visit count
    response.set_cookie('visit_count', visit_count)

    return response

def reset_visits(request):
    response = HttpResponse('Visit count has been reset.')
    response.delete_cookie('visit_count')
    return response
