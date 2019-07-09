from rest_framework import serializers
from ..models import Assessment


class AssessmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('id', 'user', 'comment', 'valuation', 'date')
