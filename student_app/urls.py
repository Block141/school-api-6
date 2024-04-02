from django.urls import path
from .views import AllStudents
# http://localhost:8000/api/v1/students/
urlpatterns = [
    path('', AllStudents.as_view(), name='all_students')
]