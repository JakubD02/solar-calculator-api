from calculator_api.models import CalculationHistory
from rest_framework import serializers

class CoordinateSerializer(serializers.Serializer):
    '''validates a single panel's top-left corner coordinates'''

    x = serializers.FloatField()
    y = serializers.FloatField()

class CalculationHistorySerializer(serializers.ModelSerializer):
    '''Serializes a stored calculation for read-only display'''

    class Meta:
        model = CalculationHistory
        fields = ["id", "input_data", "result_data"]