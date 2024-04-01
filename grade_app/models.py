from django.db import models
from student_app.models import Student
from class_app.models import Class
from .validators import validate_grade_limit
from django.core import validators as v


class Grade(models.Model):
    grade = models.DecimalField(default=100, decimal_places=2, max_digits=5, validators=[validate_grade_limit])
    a_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student} - {self.a_class} - {self.grade}"
    