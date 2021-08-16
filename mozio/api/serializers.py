from rest_framework import serializers

from core.models import *

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'

    
class PolygonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Polygon
        fields = '__all__'
