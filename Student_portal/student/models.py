from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField(unique=True)
    marks = models.FloatField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=40)
    subject = models.CharField(max_length=200)
    salary = models.IntegerField()

    