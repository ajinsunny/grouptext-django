from rest_framework import serializers
from .models import *

class TextGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TextGroup 
        fields = ('group_name', 'created_at')
    