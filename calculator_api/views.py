from calculator_api.models import CalculationHistory
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CalculationHistorySerializer, CoordinateSerializer
from solar_layout.service import SolarService

class CalculateLayoutView(APIView):
    def post(self, request):
        serializer = CoordinateSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        service = SolarService()

        try:
            result = service.calculator(serializer.validated_data)
        except (TypeError, ValueError) as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        CalculationHistory.objects.create(
            input_data=serializer.validated_data, 
            result_data=result,
        )

        return Response(result, status=status.HTTP_200_OK)
    
class CalculationHistoryListView(APIView):
    def get(self, request):
        history = CalculationHistory.objects.all()
        serializer = CalculationHistorySerializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)