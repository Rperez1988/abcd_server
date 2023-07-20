from operator import rshift
from django.db import models

# Create your models here.
class stock(models.Model):

    date     = models.DateField(('Date'), auto_now=False)
    open     = models.FloatField(('Open'), max_length=255)
    close    = models.FloatField(('Close'), max_length=255)
    high     = models.FloatField(('High'), max_length=255)
    low      = models.FloatField(('Low'), max_length=255)
    adjClose = models.FloatField(('Adj Close'), max_length=255)
    volume   = models.FloatField(('Volume'), max_length=255)
    symbol   = models.CharField(('Symbol'), max_length=255)

class strategyResults(models.Model):
    active      = models.CharField(('active'), max_length=255)
    stock       = models.CharField(('stock'), max_length=255)
    length      = models.CharField(('total_open'), max_length=255)
    total_open  = models.CharField(('total_open'), max_length=255)
    total_close = models.CharField(('total_close'), max_length=255)
    total_won   = models.CharField(('total_won'), max_length=255)
    total_lost  = models.CharField(('total_lost'), max_length=255)
    pnl         = models.CharField(('pnl'), max_length=255)
    strike_rate = models.CharField(('strike_rate'), max_length=255)
    largestWin  = models.CharField(('largestWin'), max_length=255)
    largestLost  = models.CharField(('largestLost'), max_length=255)

class strategySettings(models.Model):
    length          = models.CharField(('length'), max_length=255)
    lowrestriction  = models.CharField(('low restriction'), max_length=255)
    stock           = models.CharField(('stock'), max_length=255)

class tradeResults(models.Model):
    tradeid                     = models.CharField(('tradeid'), max_length=255)
    stock                       = models.CharField(('stock'), max_length=255)
    trade_complete              = models.CharField(('trade_complete'), max_length=255)
    price_of_pivot_high         = models.CharField(('price_of_pivot_high'), max_length=255)
    price_of_pivot_low          = models.CharField(('price_of_pivot_low'), max_length=255)
    date_of_pivot_high          = models.CharField(('date_of_pivot_high'), max_length=255)
    date_of_pivot_low           = models.CharField(('date_of_pivot_low'), max_length=255)
    date_pivot_high_snr_tested  = models.CharField(('date_pivot_high_snr_tested'), max_length=255)
    price_pivot_high_snr_tested = models.CharField(('price_pivot_high_snr_tested'), max_length=255)
    date_entered_short          = models.CharField(('date_entered_short'), max_length=255)
    price_entered_short         = models.CharField(('price_entered_short'), max_length=255)
    date_closed_short           = models.CharField(('date_closed_short'), max_length=255)
    price_closed_short          = models.CharField(('price_closed_short'), max_length=255)
    high_close_mark             = models.CharField(('high_close_mark'), max_length=255)
    low_close_mark              = models.CharField(('low_close_mark'), max_length=255)
    trade_result                = models.CharField(('trade_result'), max_length=255)
    lowest_price_went           = models.CharField(('lowest_price_went'), max_length=255)
    highest_price_went          = models.CharField(('highest_price_went'), max_length=255)
    pair_range                  = models.CharField(('pair_range'), max_length=255)
    pivot_pair                  = models.CharField(('pivot_pair'), max_length=255)
    pnl                         = models.CharField(('pnl'), max_length=255)
    trades_active               = models.CharField(('trades_active'), max_length=255)
    rsi                         = models.CharField(('rsi'), max_length=255)
    riskRewardRatio             = models.CharField(('riskRewardRatio'), max_length=255)
    risk             = models.CharField(('risk'), max_length=255)
    reward             = models.CharField(('reward'), max_length=255)
                 
class chartImage(models.Model):
    image = models.ImageField(upload_to='media/images/')
    
class totalResults(models.Model):

    tested   = models.CharField(('tested'), max_length=255)
    totalOpen   = models.CharField(('totalOpen'), max_length=255)
    totalClosed = models.CharField(('totalClosed'), max_length=255)
    totalWon    = models.CharField(('totalWon'), max_length=255)
    totalLost   = models.CharField(('totalLost'), max_length=255)
    totalPnl    = models.CharField(('totalPnl'), max_length=255)
    totalWr     = models.CharField(('totalWr'), max_length=255)
    largestWin    = models.CharField(('largestWin'), max_length=255)
    largestLost  = models.CharField(('largestLost'), max_length=255)
    avgWin    = models.CharField(('avgWin'), max_length=255)
    avgLost     = models.CharField(('avgLost'), max_length=255)
    avgTrade     = models.CharField(('avgTrade'), max_length=255)
    longestTrade  = models.CharField(('longestTrade'), max_length=255)
    shortestTrade    = models.CharField(('shortestTrade'), max_length=255)
    longestOneToTwo     = models.CharField(('longestOneToTwo'), max_length=255)
    shortestOneToTwo     = models.CharField(('shortestOneToTwo'), max_length=255)
    avgOneToTwo     = models.CharField(('avgOneToTwo'), max_length=255)
    longestTwoToShort     = models.CharField(('longestTwoToShort'), max_length=255)
    shortestTwoToShort     = models.CharField(('shortestTwoToShort'), max_length=255)
    avgTwoToShort     = models.CharField(('avgTwoToShort'), max_length=255)

class stocksTested(models.Model):

    stock = models.CharField(('stock'), max_length=255)

class savedLists(models.Model):
    
    name    = models.CharField(('name'), max_length=255)
    stock   = models.CharField(('stock'), max_length=255)

class stockStatistics(models.Model):

    stock           = models.CharField(('stock'), max_length=255)
    totalPnl        = models.CharField(('totalPnl'), max_length=255)
    avgPnl          = models.CharField(('avgPnl'), max_length=255)
    largestWin      = models.CharField(('largestWin'), max_length=255)
    largestLost     = models.CharField(('largestLost'), max_length=255)
    avgWin          = models.CharField(('avgWin'), max_length=255)
    avgLost         = models.CharField(('avgLost'), max_length=255)
    longestTrade    = models.CharField(('longestTrade'), max_length=255)
    shortestTrade   = models.CharField(('shortestTrade'), max_length=255)
    avgTrade        = models.CharField(('avgTrade'), max_length=255)

class activeTrades(models.Model):

    tradeid = models.CharField(('tradeid'), max_length=255)
    shares_purchased = models.CharField(('shares_purchased'), max_length=255)
    date_of_pivot_high = models.CharField(('date_of_pivot_high'), max_length=255)
    date_of_pivot_low = models.CharField(('date_of_pivot_low'), max_length=255)
    price_of_pivot_high = models.CharField(('price_of_pivot_high'), max_length=255)
    price_of_pivot_low = models.CharField(('price_of_pivot_low'), max_length=255)
    pair_range = models.CharField(('pair_range'), max_length=255)
    days_between_pivots = models.CharField(('days_between_pivots'), max_length=255)
    date_pivot_high_snr_tested = models.CharField(('date_pivot_high_snr_tested'), max_length=255)
    price_pivot_high_snr_tested = models.CharField(('price_pivot_high_snr_tested'), max_length=255)
    date_entered_short = models.CharField(('date_entered_short'), max_length=255)
    price_entered_short = models.CharField(('price_entered_short'), max_length=255)
    high_close_mark = models.CharField(('high_close_mark'), max_length=255)
    low_close_mark = models.CharField(('low_close_mark'), max_length=255)
    lowest_price_went = models.CharField(('lowest_price_went'), max_length=255)
    highest_price_went = models.CharField(('highest_price_went'), max_length=255)
    pnl = models.CharField(('pnl'), max_length=255)
    cash_invested = models.CharField(('cash_invested'), max_length=255)
    current_cash_in_hand = models.CharField(('current_cash_in_hand'), max_length=255)
    trades_active = models.CharField(('trades_active'), max_length=255)
    symbol = models.CharField(('symbol'), max_length=255)
    activePrice = models.CharField(('activePrice'), max_length=255)
    tradeType = models.CharField(('tradeType'), max_length=255)
    durationOfTrade = models.CharField(('tradeType'), max_length=255)
    ohlc  =  models.JSONField(null=True)


