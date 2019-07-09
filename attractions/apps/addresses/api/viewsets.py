from rest_framework.viewsets import ModelViewSet
from ..models import Address
from .serializers import AddressesSerializers


class AddressesViewSet(ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = AddressesSerializers
