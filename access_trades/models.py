from django.db import models

class TradesInChartView(models.Model):

    tradeInfo = models.JSONField(null=True)
    pivotInfo = models.JSONField(null=True)
    settings = models.JSONField(null=True)
    pnl = models.JSONField(null=True)
    retracement = models.JSONField(null=True)
    enterExitInfo = models.JSONField(null=True)
    duration = models.JSONField(null=True)
    movement = models.JSONField(null=True)
    chartData = models.JSONField(null=True)


class peformance(models.Model):

    retracement = models.JSONField(null=True)
    trades = models.JSONField(null=True)
    wins = models.JSONField(null=True)
    lost = models.JSONField(null=True)
    active = models.JSONField(null=True)
    average_price_dropped = models.JSONField(null=True)
    lowest_price_dropped = models.JSONField(null=True)
    win_pct = models.JSONField(null=True)
    rsi_wr = models.JSONField(null=True)
    volume_change_win_pct = models.JSONField(null=True)
    volume_change_lose_pct = models.JSONField(null=True)


