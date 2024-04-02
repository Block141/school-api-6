import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_proj.settings")

django.setup()


from student_app.models import Student
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.utils import DataError
from class_app.models import Class
from grade_app.models import Grade

def clear_tables():
    Student.objects.all().delete()
    Class.objects.all().delete()
    
def insert_data():
    try:
        clear_tables()
        
        Student.objects.create(
            name="Johnny H. Harris",
            student_email="thisIsMyEmail@school.com",
            personal_email="thisIsMyEmail@gmail.com",
            locker_number=108,
            locker_combination="11-11-11",
            good_student=False,
        )
        Class.objects.create(subject="Python", professor="Mrs. Zaynab")
        Class.objects.create(subject="Python2", professor="Mrs. Zaynab2")
        print("Student created successfully.")
        
        a_class = Class.objects.create(
            subject="a subject", professor="Professor Ben"
        )
        a_class.save()
        a_class.add_a_student(Student.objects.all().first().id)
        
    except (ValidationError, IntegrityError, DataError) as e:
        print(f"Error occurred while creating student: {e}")

insert_data()


