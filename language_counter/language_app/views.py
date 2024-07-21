from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def count_languages(request):
    if request.method == 'POST':
        selected_languages = request.POST.getlist('languages')
        count = len(selected_languages)
        return JsonResponse({'count': count})
    return JsonResponse({'count': 0})
