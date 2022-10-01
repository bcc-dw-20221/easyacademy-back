from django.urls import path, include
from rest_framework import routers

from ults.views import (
    SectorViewSet, 
    ClassRoomViewSet, 
    SubjectViewSet, 
    JobViewSet,
    CourseViewSet,
)

router = routers.DefaultRouter()
router.register(r'setores', SectorViewSet)
router.register(r'salas', ClassRoomViewSet)
router.register(r'disciplinas', SubjectViewSet)
router.register(r'vagas', JobViewSet)
router.register(r'cursos', CourseViewSet),

urlspattern = [
    path("", include(router.urls)),
]

