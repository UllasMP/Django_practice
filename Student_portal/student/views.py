from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    return render(request,'home.html')

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll_no')
        mark = request.POST.get("marks")
        sub = request.POST.get("subject")
        Student.objects.create(name = name, roll_no = roll, marks = mark, subject = sub)

    return render(request,'create.html')

def display(request):
    stu = Student.objects.all()
    context = {"student":stu}
    return render(request,'display.html',context)