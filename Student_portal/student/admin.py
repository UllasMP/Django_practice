from django.contrib import admin
from .models import Student, Teacher
# Register your models here.



class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id",'name','subject','salary')
admin.site.register(Teacher,TeacherAdmin)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id","name", 'roll_no','marks', 'subject')