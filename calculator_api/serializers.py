from rest_framework import serializers

class CoordinateSerializer(serializers.Serializer):
    '''validates a single panel's top-left corner coordinates'''

    x = serializers.FloatField()
    y = serializers.FloatField()