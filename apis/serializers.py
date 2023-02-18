from rest_framework import serializers
from .models import ThresholdValue
from rest_framework.settings import api_settings

class RangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThresholdValue
        fields = '__all__'
