from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from django.core.serializers import serialize
import json


class AllStudents(APIView):
    def get(self, request):
        students = Student.objects.order_by("name")
        serialized_students = serialize("json", students)
        json_students = json.loads(serialized_students)
        return Response(json_students)
