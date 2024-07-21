from django.shortcuts import render
from django.http import HttpResponse
from collections import Counter

def find_mode(request, numbers):
    # Split the numbers by comma and convert to integers
    number_list = list(map(int, numbers.split(',')))
    
    # Find the mode using Counter
    number_counts = Counter(number_list)
    max_count = max(number_counts.values())
    mode = [num for num, count in number_counts.items() if count == max_count]

    context = {
        'numbers': number_list,
        'mode': mode,
    }
    
    return render(request, 'analysis_app/mode.html', context)
