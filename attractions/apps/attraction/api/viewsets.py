from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from ..models import Attraction
from .serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):

    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'description')
    ordering_fields = ('name', 'description')

