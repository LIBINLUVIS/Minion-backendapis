from rest_framework import serializers
from .models import ThresholdValue
from rest_framework.settings import api_settings

class RangeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThresholdValue
        fields = ('value','id')
