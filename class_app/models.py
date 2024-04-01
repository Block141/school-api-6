from django.db import models
from student_app.models import Student
from django.core.exceptions import ValidationError
from django.core import validators as v
from .validators import validate_subject_format, validate_professor_name

class Class(models.Model):
    subject = models.CharField(max_length=255, unique=True, validators=[validate_subject_format])
    professor = models.CharField(max_length=255, validators=[validate_professor_name])
    students = models.ManyToManyField(Student, related_name='classes')
    
    def __str__(self):
        return f"{self.subject} - {self.professor} - {self.students.count()}"

    def add_a_student(self, student_id):
        student = Student.objects.get(pk=student_id)
        self.students.add(student)
        
    def drop_a_student(self, student_id):
        student = Student.objects.get(pk=student_id)
        self.students.remove(student)
        
    def clean(self):
        if self.students.count() < 1 or self.students.count() > 30:
            raise ValidationError('A class must have between 1 and 30 students')
        

            