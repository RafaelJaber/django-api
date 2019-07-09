from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from attractions.apps.core.api.viewsets import TouristSpotViewSet
from attractions.apps.attraction.api.viewsets import AttractionViewSet


router = routers.DefaultRouter()
router.register(r'tourist-spot', viewset=TouristSpotViewSet)
router.register(r'attraction', viewset=AttractionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
