from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ults.views import SectorViewSet

router= routers.DefaultRouter()
router.register(r'setores', SectorViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
