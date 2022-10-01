from rest_framework import viewsets
from .models import Student, Teacher
from .serializers import (
   StudentSerializer,
   TeacherSerializer,
   UserSerializer,
)
from django.contrib.auth import get_user_model

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class StudentViewSet(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer
   
class TeacherViewSet(viewsets.ModelViewSet):
   queryset = Teacher.objects.all()
   serializer_class = TeacherSerializer