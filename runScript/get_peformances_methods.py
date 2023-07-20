import statistics

def get_wins_losses_active_amount(trade):

    active = 0
    wins = 0
    lost = 0

    if trade['tradeInfo']["tradeResult"] == 'Win':
        wins += 1

    if trade['tradeInfo']["tradeResult"] == "Loss":
        lost += 1
    
    if trade['tradeInfo']["tradeResult"] == "Live":
        active += 1

    return active, wins, lost

def get_lowest_price_dropped_pct_on_win(trade):
    
    entry = float(trade['enterExitInfo']['enterPrice'])

    stop_loss = float(trade['pnl']['stopLoss'])

    price_dropped = float(trade['tradeInfo']['lowest_price_dropped'])

    percentage_drop = ((entry - price_dropped) / (entry - stop_loss)) * 100

    lowest_price_dropped = '%.2f'%(percentage_drop)

    return percentage_drop, lowest_price_dropped
    
def get_win_pct(wins, lost):

    if (wins + lost) > 0:            
        return '%.2f'%((wins / (wins + lost)) * 100)
            
    else: 

        return 0

def get_avg_lowest_price_dropped_on_win(wins, all_price_drops):

    if wins > 0:
        return '%.2f'%(statistics.mean(all_price_drops))

    else:
        return 0
