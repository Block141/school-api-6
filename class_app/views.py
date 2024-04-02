from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Class
from django.core.serializers import serialize
import json


class AllClasses(APIView):
    def get(self, request):
        class_name = Class.objects.order_by("subject")
        serialized_classes = serialize("json", class_name)
        json_classes = json.loads(serialized_classes)
        return Response(json_classes)