from rest_framework import viewsets
from .models import Sector, ClassRoom, Subject, Job
from .serializers import SectorSerializer, ClassRoomSerializer, SubjectSerializer, JobSerializer

class SectorViewSet(viewsets.ModelViewSet):
   queryset = Sector.objects.all()
   serializer_class = SectorSerializer

class ClassRoomViewSet(viewsets.ModelViewSet):
   queryset = ClassRoom.objects.all()
   serializer_class = ClassRoomSerializer

class SubjectViewSet(viewsets.ModelViewSet):
   queryset = Subject.objects.all()
   serializer_class = SubjectSerializer

class JobViewSet(viewsets.ModelViewSet):
   queryset = Job.objects.all()
   serializer_class = JobSerializer
