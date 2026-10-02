from django.shortcuts import render,redirect
from .models import Student
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def validate_student_data(name, roll_no, marks, subject, student_id=None):
    """Return cleaned values and validation errors for student submissions."""
    name = name.strip()
    roll_no = roll_no.strip()
    marks = marks.strip()
    subject = subject.strip()
    errors = []

    if not name.isalpha():
        errors.append("Name must contain characters only.")
    elif not 3 <= len(name) <= 15:
        errors.append("Name must be between 4 and 15 characters.")

    if not (len(roll_no) == 4 and roll_no.isascii() and roll_no.isdigit()):
        errors.append("Roll number must contain exactly 4 digits.")
    else:
        existing_roll = Student.objects.filter(roll_no=int(roll_no))
        if student_id is not None:
            existing_roll = existing_roll.exclude(id=student_id)
        if existing_roll.exists():
            errors.append("This roll number already exists.")

    if not (marks.isascii() and marks.isdigit()):
        errors.append("Marks must be a whole number without decimals.")
    elif int(marks) > 100:
        errors.append("Marks must be less than or equal to 100.")

    if  not 3 <= len(subject) <= 15:
        errors.append("Subject must be between 3 and 15 characters.")

    return name, roll_no, marks, subject, errors


def home(request):
    return render(request,'home.html')

def create(request):
    if request.method == 'POST':
        name, roll, mark, sub, errors = validate_student_data(
            request.POST.get('name', ''),
            request.POST.get('roll_no', ''),
            request.POST.get('marks', ''),
            request.POST.get('subject', ''),
        )
        if errors:
            for error in errors:
                messages.error(request, error)
            student = Student(name=name, roll_no=roll, marks=mark, subject=sub)
            return render(request, 'create.html', {'op': 'Create Student', 'student': student})
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
        name, roll, marks, sub, errors = validate_student_data(
            request.POST.get('name', ''),
            request.POST.get('roll_no', ''),
            request.POST.get('marks', ''),
            request.POST.get('subject', ''),
            student.id,
        )
        if errors:
            for error in errors:
                messages.error(request, error)
            student.name = name
            student.roll_no = roll
            student.marks = marks
            student.subject = sub
            return render(request, 'update.html', {'student': student, 'op': 'update'})

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
