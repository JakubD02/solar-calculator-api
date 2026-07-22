from calculator_api.models import CalculationHistory
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CalculationHistorySerializer, CoordinateSerializer
from solar_layout.service import SolarService
from django.shortcuts import get_object_or_404

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
    
class CalculationListView(APIView):
    def get(self, request):
        calculations = CalculationHistory.objects.all()
        serializer = CalculationHistorySerializer(calculations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CalculationDetailView(APIView):
    def get(self, request, pk):
        calculation = get_object_or_404(CalculationHistory, pk=pk)
        serializer = CalculationHistorySerializer(calculation)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CalculationMountsView(APIView):
    def get(self, request, pk):
        history = get_object_or_404(CalculationHistory, pk=pk)
        mounts = history.result_data.get("mounts", [])
        return Response({"mounts": mounts}, status=status.HTTP_200_OK)

class CalculationJointsView(APIView):
    def get(self, request, pk):
        history = get_object_or_404(CalculationHistory, pk=pk)
        joints = history.result_data.get("joints", [])
        return Response({"joints": joints}, status=status.HTTP_200_OK)