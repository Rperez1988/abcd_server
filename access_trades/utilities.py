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

def get_lowest_price_dropped_pct_on_win(trade, lowest_price_dropped):
    
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

def get_average_length(trade):
    return

def get_all_selected_cd_retracement_data(request, all_trades):

    # Get selected bc.
    request_param = getBodyContext(request, 'bc')
    
    # Split selected bc.
    gt_value, lt_value = request_param.split('-')

    # Convert the split parts to integers
    gt_value = int(gt_value)
    lt_value = int(lt_value)

    # Filter the all_trades objects based on the extracted values
    filtered_trades = list(all_trades.objects.filter(retracement__bcRetracement__gt=gt_value, retracement__bcRetracement__lt=lt_value))

    return filtered_trades

def putTradesIntoCorrectCDList(filtered_trades):
    
    # Create Object of each cd retracement range as the key.
    retracemnts = {f'{i}-{i+1}': [] for i in range(100,500)}


    # Organize all the trades into their corresponding range.
    for eachTrade in list(filtered_trades):

        # Convert object from django model object to python object.
        singleTrade = eachTrade.__dict__

        # Get cd retracement of current trade.
        cd_retracement = singleTrade['retracement']['cdRetracement']

        # Calculate the cd retracement (range) for the current cdRetracement value.
        key = f'{int(cd_retracement)}-{int(cd_retracement) + 1}'
        
        # Append the trade object to the corresponding range.
        retracemnts[key].append(singleTrade)

    return retracemnts

def getBodyContext(request, str):

    body_unicode = request.body.decode('utf-8')
    
    import ast
    d = ast.literal_eval(body_unicode)

    return (d[str])

