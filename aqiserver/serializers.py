from .models import *
from rest_framework import serializers

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class AqimonthdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aqimonthdata
        depth = 2
        fields = '__all__'

class AqidaydataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aqidaydata
        depth = 2
        fields = "__all__"
