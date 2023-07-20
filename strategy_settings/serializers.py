# todos/serializers.py
from rest_framework import serializers
from .models import strategySettings


class StrategySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = strategySettings
        fields = '__all__'

