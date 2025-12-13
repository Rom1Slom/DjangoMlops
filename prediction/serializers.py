from rest_framework import serializers

class PredictionInputSerializer(serializers.Serializer):
    date = serializers.DateField()
    predicted_consumption = serializers.FloatField()

