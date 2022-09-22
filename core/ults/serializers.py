from dataclasses import field, fields
from .models import Sector, ClassRoom, Subject, Job
from rest_framework import serializers

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['name']

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'floor','number']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title']