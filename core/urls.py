from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from entities.views import (
    StudentViewSet,
    UserViewSet,
)

router= routers.DefaultRouter()

router.register(r'estudantes', StudentViewSet),
router.register(r'usuarios', UserViewSet),

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('ults/', include("ults.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
