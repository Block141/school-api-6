from django.db import models
from student_app.models import Student
from class_app.models import Class
from django.core import validators as v


class Grade(models.Model):
    grade = models.DecimalField(default=100, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])
    a_class = models.ForeignKey(Class)
    student = models.ForeignKey(Student)
    
    def __str__(self):
        return f"{self.student} - {self.a_class} - {self.grade}"