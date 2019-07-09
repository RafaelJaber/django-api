from rest_framework import serializers
from ..models import Address


class AddressesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('street', 'city', 'state', 'country', 'latitude', 'longitude')
