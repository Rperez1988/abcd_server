from rest_framework import serializers
from .models import *


class Pattern_A_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern_A
        fields = '__all__'

class Pattern_AB_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern_AB
        fields = '__all__'

class Pattern_ABC_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern_ABC
        fields = '__all__'

class Pattern_ABCD_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern_ABCD
        fields = '__all__'


class Selected_ABCD_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Selected_ABCD
        fields = '__all__'


