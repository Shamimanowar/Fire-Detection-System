from rest_framework import serializers
from .models import FireDetector


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireDetector
        fields = '__all__'
