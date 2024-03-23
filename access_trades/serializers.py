from rest_framework import serializers
from .models import TradesInChartView, peformance, cd_pef, cd_Peformance, by_symbols


class TradesInChartViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradesInChartView
        fields = '__all__'

class PeformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = peformance
        fields = '__all__'

class CDPeformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = cd_pef
        fields = '__all__'

class CDPeformance(serializers.ModelSerializer):
    class Meta:
        model = cd_Peformance
        fields = '__all__'


class BySymbolsSerialilzer(serializers.ModelSerializer):
    class Meta:
        model = by_symbols
        fields = '__all__'