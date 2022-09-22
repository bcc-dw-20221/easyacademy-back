from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ults.views import SectorViewSet,ClassRoomViewSet, SubjectViewSet, JobViewSet

router= routers.DefaultRouter()
router.register(r'setores', SectorViewSet)
router.register(r'salas', ClassRoomViewSet)
router.register(r'disciplinas', SubjectViewSet)
router.register(r'vagas', JobViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
