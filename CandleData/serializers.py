from rest_framework import serializers
from .models import *

class CandleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (

            'candle_id', 
            'symbol',
            'candle_date', 
            'candle_open',
            'candle_close', 
            'candle_high',
            'candle_low',  
            

        )
        model = Candle

class SymbolInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SymbolInfo
class SelectedCandlesAPI(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SelectedCandles
