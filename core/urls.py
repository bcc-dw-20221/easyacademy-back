from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ults.views import (
    SectorViewSet,
    ClassRoomViewSet,
    SubjectViewSet,
    JobViewSet,
    CourseViewSet,
    ClassHoursViewSet,
)
from entities.views import (
    StudentViewSet,
    UserViewSet,
    TeacherViewSet,
)

router= routers.DefaultRouter()
router.register(r'setores', SectorViewSet)
router.register(r'horarios', ClassHoursViewSet)
router.register(r'salas', ClassRoomViewSet)
router.register(r'disciplinas', SubjectViewSet)
router.register(r'vagas', JobViewSet)
router.register(r'cursos', CourseViewSet)

router.register(r'usuarios', UserViewSet),
router.register(r'estudantes', StudentViewSet),
router.register(r'professores', TeacherViewSet),

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('ults/', include("ults.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
