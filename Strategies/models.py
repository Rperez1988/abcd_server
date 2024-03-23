from django.db import models
import uuid

class Strategies(models.Model):

    strategy_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    total_return = models.FloatField()
    total_win_percentage = models.FloatField()
    initial_cash_investment = models.FloatField()
    current_cash_investment = models.FloatField()
    total_trades = models.IntegerField()
    average_trade_duration_days = models.IntegerField()



