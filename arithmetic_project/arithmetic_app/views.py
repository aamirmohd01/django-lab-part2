from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def evaluate_expression(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        try:
            # Evaluate the expression
            result = eval(expression)
            return JsonResponse({'result': result, 'success': True})
        except Exception as e:
            return JsonResponse({'result': str(e), 'success': False})
    return JsonResponse({'result': 'Invalid request', 'success': False})
