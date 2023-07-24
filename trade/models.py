from django.db import models

class all_trades(models.Model):

    

    tradeInfo = models.JSONField(null=True, max_length=254)
    pivotInfo = models.JSONField(null=True, max_length=254)
    settings = models.JSONField(null=True, max_length=254)
    pnl = models.JSONField(null=True, max_length=254)
    retracement = models.JSONField(null=True, max_length=254)
    enterExitInfo = models.JSONField(null=True, max_length=254)
    duration = models.JSONField(null=True, max_length=254)
    movement = models.JSONField(null=True, max_length=254)
    chartData = models.JSONField(null=True, max_length=254)
    length = models.JSONField(null=True, max_length=254)

    def __repr__(self):
        return f"(tradeInfo={self.tradeInfo}, pivotInfo={self.pivotInfo}, settings={self.settings}, pnl={self.pnl}, retracement={self.retracement}, enterExitInfo={self.enterExitInfo}, duration={self.duration}, movement={self.movement}, chartData={self.chartData})"

  