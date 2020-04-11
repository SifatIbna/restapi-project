from rest_framework import serializers

from status.models import Status

'''
    Serializer --> JSON
    Serializer --> validate data
'''

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user', 
            'content',
            'image'
        ]
