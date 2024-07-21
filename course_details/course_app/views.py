from django.shortcuts import render
from course_app.models import Subjects
from django.shortcuts import redirect

# Create your views here.
def subject_list(request):
    subjects = Subjects.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def home(request):
    return redirect('subject_list')
