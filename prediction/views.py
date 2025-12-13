from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta
from .serializers import PredictionInputSerializer
# Create your views here.


class PredictionView(APIView):
    def get(self, request):
        # Example: Generate predictions for the next day
        import datetime
        today = datetime.date.today()
        predicted_value = 100  # Dummy prediction logic
        data = {
            'date': today + timedelta(days=1),
            'predicted_consumption': predicted_value
        }
        serializer = PredictionInputSerializer(data)
        return Response(serializer.data)