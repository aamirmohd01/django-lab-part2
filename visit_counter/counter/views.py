from django.shortcuts import render
from django.http import HttpResponse

def visit_count_view(request):
    # Get the current visit count from cookies, defaulting to 0 if not found
    visit_count = int(request.COOKIES.get('visit_count', 0))

    # Increment the visit count
    visit_count += 1

    # Create a response message based on the visit count
    if visit_count == 1:
        message = f'This is your first visit, so cookies count = {visit_count}'
    else:
        message = f'Your visited count on this page is {visit_count} times.'

    # Create a response object
    response = HttpResponse(message)

    # Set the cookie with the updated visit count
    response.set_cookie('visit_count', visit_count, max_age=365*24*60*60)  # Cookie expires in 1 year

    return response
