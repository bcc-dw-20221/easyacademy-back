from http.client import ImproperConnectionState
from rest_framework import viewsets
from .models import Student
from .serializers import (
   StudentSerializer,
   UserSerializer,
)
from django.contrib.auth import get_user_model

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    

class StudentViewSet(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer