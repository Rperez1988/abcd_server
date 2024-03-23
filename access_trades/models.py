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
    average_length_win = models.JSONField(null=True)
    average_length = models.JSONField(null=True)


class cd_pef(models.Model):
    
    bc = models.JSONField(null=True)
    cd = models.JSONField(null=True)
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
    average_length_win = models.JSONField(null=True)
    average_length = models.JSONField(null=True)


class cd_Peformance(models.Model):

    bc_retracement_range = models.IntegerField()
    cd_retracement_range = models.IntegerField()
    trades = models.IntegerField()
    wins = models.IntegerField()
    lost = models.IntegerField()
    active = models.IntegerField()
    average_price_dropped = models.IntegerField()
    lowest_price_dropped = models.IntegerField()
    win_pct = models.IntegerField()
    rsi_wr = models.IntegerField()
    volume_change_win_pct = models.IntegerField()
    volume_change_lose_pct = models.IntegerField()
    average_length_win = models.IntegerField()
    average_length = models.IntegerField()

class by_symbols(models.Model):

    symbol = models.CharField(max_length=255)
    amount = models.IntegerField()
    winpct = models.CharField(max_length=100)
    won = models.IntegerField()
    lost = models.IntegerField()
    live = models.IntegerField()


    def __str__(self):
        return f"Symbol: {self.symbol}, Amount: {self.amount}, Win Percentage: {self.winpct}"