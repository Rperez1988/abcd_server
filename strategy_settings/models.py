from django.db import models

class strategySettings(models.Model):

    id = models.AutoField(primary_key=True)
    symbol = models.TextField('symbol', max_length=25)
    settingsName = models.TextField('settingsName', max_length=25)
    market = models.CharField('market', max_length=25)
    pivotLength = models.CharField('pivotLength', max_length=25)
    rrr = models.CharField('rrr', max_length=25)
    sAndr = models.CharField('aToBLength', max_length=25)
    maxAtoBLength = models.CharField('bToShortLength', max_length=25)
    maxBtoCLength = models.CharField('marketType', max_length=25)
    maxCtoDLength = models.CharField('singlePivot', max_length=25)
    entryRSI = models.CharField('isRsiActive', max_length=25)
    abnormalPriceJump = models.CharField('rsi', max_length=25)
    pivotSteepness = models.CharField('isPivotSteepnessActive', max_length=25)
    aBelowB = models.CharField('isAbnormalPriceActive', max_length=25)
    isComplete = models.CharField('isComplete', max_length=25)
    isSelected =  models.CharField('isComplete', max_length=25)
    startDate = models.CharField('startDate', max_length=25)
    endDate = models.CharField('endDate', max_length=25)




  

