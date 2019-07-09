from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from attractions.apps.core.api.viewsets import TouristSpotViewSet


router = routers.DefaultRouter()
router.register(r'tourist-spot', viewset=TouristSpotViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
