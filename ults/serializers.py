from dataclasses import field
from pyexpat import model
from .models import ClassHours, Course, Sector, ClassRoom, Subject, Job
from rest_framework import serializers

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id', 'name']

class ClassHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassHours
        fields = ['id', 'day_week', 'time_class', 'class_shift']

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'floor','number']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'teacher']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'coordenador']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title']