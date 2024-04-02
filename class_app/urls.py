from django.urls import path
from .views import AllClasses
# http://localhost:8000/api/v1/classess/
urlpatterns = [
    # Currently only takes GET requests
    path('', AllClasses.as_view(), name='all_classes')
]