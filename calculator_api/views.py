from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CoordinateSerializer
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
        
        return Response(result, status=status.HTTP_200_OK)