from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ults.views import (
    SectorViewSet,
    ClassRoomViewSet,
    SubjectViewSet,
    JobViewSet,
    CourseViewSet,
)
from entities.views import (
    StudentViewSet,
    UserViewSet,
    TeacherViewSet
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router= routers.DefaultRouter()
router.register(r'setores', SectorViewSet)
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
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
 ]

