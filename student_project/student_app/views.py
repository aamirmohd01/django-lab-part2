from django.http import HttpResponse 
from django.shortcuts import render
from student_app.models import Course, Student 
# student = Student.objects.create(student_usn ="111",student_name="ABCD",student_sem=5)
def reg(request):
    if request.method == "POST":
        sid=request.POST.get("sname") 
        cid=request.POST.get("cname") 
        student=Student.objects.get(id=sid) 
        course=Course.objects.get(id=cid) 
        res=student.enrolment.filter(id=cid) 
        if res:
            return HttpResponse("<h1>Student already enrolled</h1>") 
        student.enrolment.add(course)
        return HttpResponse("<h1>Student enrolled successfully</h1>")

    else:
        students=Student.objects.all()
        courses=Course.objects.all()
        return render(request,"reg.html",{"students":students, "courses":courses})
