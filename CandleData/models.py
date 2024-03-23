from django.db import models
import uuid

class Candle(models.Model):
    candle_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    symbol = models.CharField(max_length=100)    
    candle_date = models.DateField()
    candle_open = models.FloatField()
    candle_high = models.FloatField()
    candle_low = models.FloatField()
    candle_close = models.FloatField()
    candle_volume = models.FloatField()

    class Meta:
        unique_together = ['symbol', 'candle_date']
    

    def __str__(self):
        return f"Candle {self.candle_id}: Symbol={self.symbol}, Date={self.candle_date}, Open={self.candle_open}, High={self.candle_high}, Low={self.candle_low}, Close={self.candle_close}, Volume={self.candle_volume}"

class SymbolInfo(models.Model):

    symbol = models.CharField(max_length=500, null=True)
    name = models.CharField(max_length=500, null=True)
    exchange = models.CharField(max_length=500, null=True)
    assetType = models.CharField(max_length=500, null=True)
    ipoDate = models.CharField(max_length=500, null=True)
    delistingDate = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=500, null=True)

    class Meta:
        unique_together = ['symbol', 'name', 'exchange','assetType', 'ipoDate', 'delistingDate']

class SelectedCandles(models.Model):
    trade_id = models.IntegerField()
    symbol = models.CharField(max_length=100)    
    candle_date = models.DateField()
    candle_open = models.FloatField()
    candle_high = models.FloatField()
    candle_low = models.FloatField()
    candle_close = models.FloatField()
    candle_volume = models.FloatField()