from django.db import models
from django.core import validators as v
from .validators import validate_name_format, validate_school_email, validate_combination_format

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, validators=[validate_name_format])
    student_email = models.EmailField(max_length=255, unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(max_length=255, unique=True, null=True)
    locker_number = models.IntegerField(default=110, unique=True, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(max_length=255, default="12-12-12", validators=[validate_combination_format])
    good_student = models.BooleanField(default=False, null=False)
    
    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    def locker_reassignment(self, update_locker_number):
        self.locker_number = update_locker_number
        self.save()

    def student_status(self, student_status):
        self.good_student = student_status
        self.save()