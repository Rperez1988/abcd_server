from rest_framework import serializers
from .models import TradesInChartView, peformance


class TradesInChartViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradesInChartView
        fields = '__all__'

class PeformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = peformance
        fields = '__all__'