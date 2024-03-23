from django.db import models
from all_patterns.models import *
from rest_framework import serializers
from rest_framework import generics
# Create your models here.
class All_Patterns_Info(models.Model):


    symbol = models.CharField(max_length=100, unique=True, null=True)
    total_abcds = models.IntegerField(null=True)
    passed_abcds = models.IntegerField(null=True)
    failed_abcds = models.IntegerField(null=True)
    open_abcds = models.IntegerField(null=True)
    passed_pct = models.FloatField(null=True)
    abcd_length = models.IntegerField(null=True)
    lowest_price_drop = models.FloatField(null=True)
    average_lowest_price_drop = models.FloatField(null=True)
    average_C_retracement = models.FloatField(null=True)
    abcd_instances = models.ManyToManyField(Pattern_ABCD, related_name='all_patterns_info', blank=True)

    class Meta:
        unique_together = ['symbol']

    def __str__(self) -> str:
        return self.symbol

class All_Patterns_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = All_Patterns_Info
        fields = '__all__'
        
class All_Patterns_Serializer(generics.ListCreateAPIView):
    queryset            = All_Patterns_Info.objects.all()
    serializer_class    = All_Patterns_Info_Serializer