from rest_framework import viewsets
from .models import (
   Course, 
   Sector, 
   ClassRoom, 
   Subject, 
   Job, 
   ClassHours,
)
from .serializers import (
   SectorSerializer, 
   ClassHoursSerializer, 
   ClassRoomSerializer, 
   SubjectSerializer,
   JobSerializer, 
   CourseSerializer, 
)


class SectorViewSet(viewsets.ModelViewSet):
   queryset = Sector.objects.all()
   serializer_class = SectorSerializer


class ClassHoursViewSet(viewsets.ModelViewSet):
   queryset = ClassHours.objects.all()
   serializer_class = ClassHoursSerializer

class ClassRoomViewSet(viewsets.ModelViewSet):
   queryset = ClassRoom.objects.all()
   serializer_class = ClassRoomSerializer


class SubjectViewSet(viewsets.ModelViewSet):
   queryset = Subject.objects.all()
   serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = CourseSerializer


class JobViewSet(viewsets.ModelViewSet):
   queryset = Job.objects.all()
   serializer_class = JobSerializer
