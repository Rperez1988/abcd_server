from django.db import models

class all_trades(models.Model):

    

    tradeInfo = models.JSONField(null=True)
    pivotInfo = models.JSONField(null=True)
    settings = models.JSONField(null=True)
    pnl = models.JSONField(null=True)
    retracement = models.JSONField(null=True)
    enterExitInfo = models.JSONField(null=True)
    duration = models.JSONField(null=True)
    movement = models.JSONField(null=True)
    chartData = models.JSONField(null=True)
    length = models.JSONField(null=True)

    def __repr__(self):
        return f"(tradeInfo={self.tradeInfo}, pivotInfo={self.pivotInfo}, settings={self.settings}, pnl={self.pnl}, retracement={self.retracement}, enterExitInfo={self.enterExitInfo}, duration={self.duration}, movement={self.movement}, chartData={self.chartData})"

  