from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from ..models import TouristSpot
from attractions.apps.attraction.api.serializers import AttractionSerializer
from attractions.apps.addresses.api.serializers import AddressesSerializers
from attractions.apps.comments.api.serializers import CommentSerializers
from attractions.apps.assessments.api.serializers import AssessmentSerializers


class TouristSpotSerializer(serializers.ModelSerializer):

    attractions = AttractionSerializer(many=True)
    address = AddressesSerializers()
    comment = CommentSerializers(many=True)
    assessment = AssessmentSerializers(many=True)

    full_description = SerializerMethodField()

    class Meta:
        model = TouristSpot
        fields = (
            'id', 'name', 'description', 'status', 'photo',
            'attractions', 'comment', 'assessment', 'address',
            'full_description'
        )

    def get_full_description(self, obj):
        return '%s - %s' % (obj.name, obj.description)