from django.shortcuts import render,redirect
from .models import Student
from django.http import HttpResponse
from django.contrib import messages

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
        messages.success(request, "Student created successfully!")
        return redirect('display')
    context = {'op':"Create Student"}
    return render(request,'create.html', context)

def display(request):
    stu = Student.objects.all()
    context = {"student":stu}
    return render(request,'display.html',context)

def update(request,student_id):
    try:
        student = Student.objects.get(id = student_id)
    except Student.DoesNotExist:
        return HttpResponse('<h1>Not Found<h1>')

    if request.method == 'POST':
        name = request.POST.get('name','')
        roll = request.POST.get('roll_no','')
        marks = request.POST.get('marks','')
        sub = request.POST.get('subject','')

        student.name = name
        student.roll_no = roll
        student.marks = marks
        student.subject = sub
        student.save()
        messages.success(request, "Student updated successfully!")
        return redirect('display')

    context = {"student":student,'op':"update"}
    return render(request,'update.html',context)

def delete(request,student_id):
    try:
        student = Student.objects.get(id = student_id)
    except Student.DoesNotExist:
        return HttpResponse('''<h1>Student not found</h1>''')

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect('display')
    
    context = {"student":student,}
    return render(request,'delete.html',context)
