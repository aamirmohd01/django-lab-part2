from django.http import HttpResponse
from django.shortcuts import render

def square_pairs(request, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    pairs = [(i, j, i**2, j**2) for i in range(1, num1 + 1) for j in range(1, num2 + 1)]
    return render(request, 'squares_app/squares.html', {'pairs': pairs})
