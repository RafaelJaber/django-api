from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from attractions.apps.core.api.viewsets import TouristSpotViewSet
from attractions.apps.attraction.api.viewsets import AttractionViewSet
from attractions.apps.addresses.api.viewsets import AddressesViewSet
from attractions.apps.comments.api.viewsets import CommentViewSet
from attractions.apps.assessments.api.viewsets import AssessmentViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'tourist-spots', viewset=TouristSpotViewSet, base_name='TouristSpot')
router.register(r'attractions', viewset=AttractionViewSet)
router.register(r'addresses', viewset=AddressesViewSet)
router.register(r'comments', viewset=CommentViewSet)
router.register(r'assessments', viewset=AssessmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
