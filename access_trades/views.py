from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from trade.models import all_trades
from access_trades.models import TradesInChartView, peformance, cd_pef, cd_Peformance, by_symbols
from .serializers import BySymbolsSerialilzer, TradesInChartViewSerializer, PeformanceSerializer, CDPeformanceSerializer, CDPeformance
from rest_framework import generics
import statistics
from . import utilities

# CREATE A BY-SYMBOL OBJECT FOR EACH SYMBOL
def create_by_symbol_object(request):

    by_symbols.objects.all().delete()
    # # Gather all trades of selected symbols
    symbol_list = ['ALT', 'AAWW']
    # all_trades = all_trades.objects.filter(symbol=symbol_list)
    all_trades_ = all_trades.objects.all()
    print('trades length: ', len(all_trades_))
    symbol_dict = {}

    # # Create symbol-dict
    for trade in all_trades_:
        symbol = trade.tradeInfo['symbol']
        if symbol not in symbol_dict:
            symbol_dict[symbol] = []
        symbol_dict[symbol].append(trade)

    # # Populate symbol-dict
    symbol_objects = []
    for key, value in symbol_dict.items():

        symbol = key
        amount = len(value)
        winpct = 0
        wins = 0
        lost = 0
        live = 0
    
        for each in value:
            print(key, each.tradeInfo['tradeResult'])
            
            if each.tradeInfo['tradeResult'] == 'Win':
                wins+=1
            if each.tradeInfo['tradeResult'] == 'Loss':
                lost+=1
            if each.tradeInfo['tradeResult'] == 'Live':
                live+=1

        if(wins > 0):
            winpct = ((wins/(wins+lost)) * 100)

        x = {
            'symbol': key,
            'amount': amount,
            'winpct': '%.2f'%winpct,
            'won': wins,
            'lost': lost,
            'live': live
    
        }
        symbol_objects.append(x)
      
    # Create symbol-object
    for symbol_object in symbol_objects:

        # Create by-sybmol object for each symbol
        by_symbols.objects.get_or_create(

            symbol = symbol_object['symbol'],
            amount = symbol_object['amount'],
            winpct = symbol_object['winpct'],
            won = symbol_object['won'],
            lost = symbol_object['lost'],
            live = symbol_object['live'],
                    
                    
        )



    return HttpResponse('by_symbols')

# CREATE A SINGLE-PEFORMANCE OBJECT FOR ALL TRADES OF ALL SYMBOLS
@csrf_exempt
def create_trades_for_single_trade_table(request):

    TradesInChartView.objects.all().delete()

    bc  = utilities.getBodyContext(request, 'bc')

    numbers = bc.split('-')

    number1 = float(numbers[0].strip())
    number2 = float(numbers[1].strip())

    filtered_trades = all_trades.objects.filter(retracement__bcRetracement__gte=number1, retracement__bcRetracement__lt=number2)

    for each in filtered_trades:
        TradesInChartView.objects.create(
            tradeInfo=each.tradeInfo,
            pivotInfo=each.pivotInfo,
            movement=each.movement,
            settings=each.settings,
            pnl=each.pnl,
            retracement=each.retracement,
            enterExitInfo=each.enterExitInfo,
            duration=each.duration,
            chartData=each.chartData,
        )
    
    return HttpResponse("DELETE HISTORY")

# CREATE A SINGLE-PEFORMANCE OBJECT FOR ALL TRADES OF SELECTED SYMBOL
@csrf_exempt
def get_trades_of_selected_symbol(request):

    symbol  = utilities.getBodyContext(request, 'symbol')

    if symbol != 'All Symbols':

        trades_of_selected_symbol =  all_trades.objects.filter(tradeInfo__symbol=symbol)

        TradesInChartView.objects.all().delete()

        for each in trades_of_selected_symbol:

            TradesInChartView.objects.get_or_create(

                tradeInfo = each.tradeInfo,
                pivotInfo = each.pivotInfo,
                movement = each.movement,
                settings = each.settings,
                pnl = each.pnl,
                retracement =  each.retracement,
                enterExitInfo = each.enterExitInfo,
                duration = each.duration,
                chartData = each.chartData,
                
            )
        
    elif symbol == 'All Symbols':

        trades_of_selected_symbol = all_trades.objects.all()

        TradesInChartView.objects.all().delete()

        for each in trades_of_selected_symbol:

            TradesInChartView.objects.get_or_create(

                tradeInfo = each.tradeInfo,
                pivotInfo = each.pivotInfo,
                movement = each.movement,
                settings = each.settings,
                pnl = each.pnl,
                retracement =  each.retracement,
                enterExitInfo = each.enterExitInfo,
                duration = each.duration,
                chartData = each.chartData,
                
            )
    
    return HttpResponse("get_trades_of_selected_symbol")

# CREATE A BC-RANGE-PEFORMANCE OBJECT FOR EACH RANGE.
def create_bc_peformances(seperated_trades):

    # CLEAR PREVIOUS DATA.
    peformance.objects.all().delete() 

    def get_lowest_price_drop_and_average_price_drop(trade, lowest_price_dropped):

        # GET LOWEST PRICE WENT DURING TRADE.
        if trade['tradeInfo']["tradeResult"] == 'Win':

            percentage_drop, lpd = utilities.get_lowest_price_dropped_pct_on_win(trade, lowest_price_dropped)

            all_price_drops.append(float(percentage_drop))

            if percentage_drop > float(lowest_price_dropped):

                lowest_price_dropped = lpd

    for each_list in seperated_trades:

        active = 0
        wins = 0
        lost = 0
        lowest_price_dropped = 0
        all_price_drops = []
        lengths = []

        for trade in seperated_trades[str(each_list)]:

            # GATHER WIN, LOST, ACTIVE, DATA.
            a, w, l = utilities.get_wins_losses_active_amount(trade)
            active += a
            wins += w
            lost += l

            # GET LENGTH OF TRADE.
            lengths.append(trade['length']['abcd_length'])
            
            # GET LOWEST PRICE DROP.
            get_lowest_price_drop_and_average_price_drop(trade, lowest_price_dropped)

        win_pct = utilities.get_win_pct(wins, lost)
        average_price_dropped = utilities.get_avg_lowest_price_dropped_on_win(wins, all_price_drops)
        total_trades = wins + lost + active

        average_length = 0
        if(len(lengths) > 0):
            average_length = '%.2f'%(statistics.mean(lengths))

        peformance.objects.get_or_create(
            retracement = str(each_list),
            trades = total_trades,
            wins = wins,
            lost = lost,
            active = active,
            win_pct = str(win_pct)  + '%',
            lowest_price_dropped = str(lowest_price_dropped)  + '%',
            average_price_dropped = str(average_price_dropped) + '%',      
            rsi_wr = 0,
            volume_change_win_pct = 0,
            volume_change_lose_pct = 0,
            average_length_win = 0,
            average_length = average_length,

        )

# CREATE A CD-RANGE-PEFORMANCE OBJECT FOR EACH RANGE.
@csrf_exempt
def create_cd_peformances(request):

    # Clear any previous cd object data.
    cd_pef.objects.all().delete()

    # Get filtered trades.
    cd_retracements = utilities.get_all_selected_cd_retracement_data(request, all_trades)

    filtered_cd_list = utilities.putTradesIntoCorrectCDList(cd_retracements)
    

    # LOOP OVER EACH RANGE.
    for key, value in filtered_cd_list.items():
        
        active = 0
        wins = 0
        lost = 0

        lowest_price_dropped = 0
        all_price_drops = []
        lengths = []

        # LOOP OVER THE CURRENT RANGE-LIST OF TRADES.
        for trade in value:

            # Get result of current trade.
            a, w, l = utilities.get_wins_losses_active_amount(trade)
            active += a
            wins += w
            lost += l

            # Get length of current trade.
            lengths.append(trade['length']['abcd_length'])

            # If the current trade result is a 'Win', get the lowest the price dropped during the trade.
            if trade['tradeInfo']["tradeResult"] == 'Win':

                percentage_drop, lpd = utilities.get_lowest_price_dropped_pct_on_win(trade, lowest_price_dropped)

                all_price_drops.append(float(percentage_drop))

                if percentage_drop > float(lowest_price_dropped):

                    lowest_price_dropped = lpd
    
        win_pct = utilities.get_win_pct(wins, lost)

        average_price_dropped = utilities.get_avg_lowest_price_dropped_on_win(wins, all_price_drops)

        total_trades = wins + lost + active

        average_length = 0

        if(len(lengths) > 0):

            average_length = '%.2f'%(statistics.mean(lengths))

        # CREATE PEFORMANCE-OBJECT FOR CURRENT RANGE PEFORMANCE.
        cd_pef.objects.create(
            bc = str(key),
            cd = key,
            trades = total_trades,
            wins = wins,
            lost = lost,
            active = active,
            win_pct = str(100)  + '%',
            lowest_price_dropped = str(lowest_price_dropped)  + '%',
            average_price_dropped = str(100) + '%',      
            rsi_wr = 0,
            volume_change_win_pct = 0,
            volume_change_lose_pct = 0,
            average_length_win = 0,
            average_length = 100,

        )

    return HttpResponse("CD BACKEND")

@csrf_exempt
# GATHER ALL TRADES OF SELECTED SYMBOL
def get_all_trades_of_selected_symbol(request):

    symbol  = utilities.getBodyContext(request, 'symbol')

    filtered_trades = all_trades.objects.filter(tradeInfo__symbol=symbol)
    
    trades = seperate_trades_by_bc(filtered_trades)

    create_bc_peformances(trades)

    low = 0
    high = 100

    # Filter the all_trades objects based on the extracted values
    filtered_trades = [trade for trade in filtered_trades if low < trade.retracement['bcRetracement'] < high]
    filtered_cd_list = utilities.putTradesIntoCorrectCDList(filtered_trades)
 

    create_c(filtered_cd_list)

    TradesInChartView.objects.all().delete()   
    # Create trades of symbol
    for each in filtered_trades:
        TradesInChartView.objects.create(
            tradeInfo=each.tradeInfo,
            pivotInfo=each.pivotInfo,
            movement=each.movement,
            settings=each.settings,
            pnl=each.pnl,
            retracement=each.retracement,
            enterExitInfo=each.enterExitInfo,
            duration=each.duration,
            chartData=each.chartData,
        )
    
    return HttpResponse('get_all_trades_of_selected_symbol')

def seperate_trades_by_bc(all_trades):

    x = { 
        '0-100': [],
        '0-1': [],
        '1-2': [],
        '2-3': [],
        '3-4': [],
        '4-5': [],
        '5-6': [],
        '6-7': [],
        '7-8': [],
        '8-9': [],
        '9-10': [],
        '10-11': [],
        '11-12': [],
        '12-13': [],
        '13-14': [],
        '14-15': [],
        '15-16': [],
        '16-17': [],
        '17-18': [],
        '18-19': [],
        '19-20': [],
        '20-21': [],
        '21-22': [],
        '22-23': [],
        '23-24': [],
        '24-25': [],
        '25-26': [],
        '26-27': [],
        '27-28': [],
        '28-29': [],
        '29-30': [],
        '30-31': [],
        '31-32': [],
        '32-33': [],
        '33-34': [],
        '34-35': [],
        '35-36': [],
        '36-37': [],
        '37-38': [],
        '38-39': [],
        '39-40': [],
        '40-41': [],
        '41-42': [],
        '42-43': [],
        '43-44': [],
        '44-45': [],
        '45-46': [],
        '46-47': [],
        '47-48': [],
        '48-49': [],
        '49-50': [],
        '50-51': [],
        '51-52': [],
        '52-53': [],
        '53-54': [],
        '54-55': [],
        '55-56': [],
        '56-57': [],
        '57-58': [],
        '58-59': [],
        '59-60': [],
        '60-61': [],
        '61-62': [],
        '62-63': [],
        '63-64': [],
        '64-65': [],
        '65-66': [],
        '66-67': [],
        '67-68': [],
        '68-69': [],
        '69-70': [],
        '70-71': [],
        '71-72': [],
        '72-73': [],
        '73-74': [],
        '74-75': [],
        '75-76': [],
        '76-77': [],
        '77-78': [],
        '78-79': [],
        '79-80': [],
        '80-81': [],
        '81-82': [],
        '82-83': [],
        '83-84': [],
        '84-85': [],
        '85-86': [],
        '86-87': [],
        '87-88': [],
        '88-89' :[],
        '89-90': [],
        '90-91': [],
        '91-92': [],
        '92-93': [],
        '93-94': [],
        '94-95': [],
        '95-96': [],
        '96-97': [],
        '97-98': [],
        '98-99': [],
        '99-100': [],

}

    for each in all_trades:

        bc = float(each.retracement['bcRetracement'])

        temp = {
                'tradeInfo': each.tradeInfo,
                'pivotInfo': each.pivotInfo,
                'settings': each.settings,
                'pnl': each.pnl,
                'retracement': each.retracement,
                'enterExitInfo': each.enterExitInfo,
                'duration': each.duration,
                'movement': each.movement,
                'chartData': each.chartData,
                'length': each.length,
            
            }
    
        x['0-100'].append(temp)
        if 0 <= bc and bc < 1:
            x['0-1'].append(temp)
        elif 1 <= bc and bc < 2:
            x['1-2'].append(temp)
        elif 2 <= bc and bc < 3:
            x['2-3'].append(temp)
        elif 3 <= bc and bc < 4:
            x['3-4'].append(temp)
        elif 4 <= bc and bc < 5:
            x['4-5'].append(temp)
        elif 5 <= bc and bc < 6:
            x['5-6'].append(temp)
        elif 6 <= bc and bc < 7:
            x['6-7'].append(temp)
        elif 7 <= bc and bc < 8:
            x['7-8'].append(temp)
        elif 8 <= bc and bc < 9:
            x['8-9'].append(temp)
        elif 9 <= bc and bc < 10:
            x['9-10'].append(temp)
        elif 10 <= bc and bc < 11:
            x['10-11'].append(temp)
        elif 11 <= bc and bc < 12:
            x['11-12'].append(temp)
        elif 12 <= bc and bc < 13:
            x['12-13'].append(temp)
        elif 13 <= bc and bc < 14:
            x['13-14'].append(temp)
        elif 14 <= bc and bc < 15:
            x['14-15'].append(temp)
        elif 15 <= bc and bc < 16:
            x['15-16'].append(temp)
        elif 16 <= bc and bc < 17:
            x['16-17'].append(temp)
        elif 17 <= bc and bc < 18:
            x['17-18'].append(temp)
        elif 18 <= bc and bc < 19:
            x['18-19'].append(temp)
        elif 19 <= bc and bc < 20:
            x['19-20'].append(temp)
        elif 20 <= bc and bc < 21:
            x['20-21'].append(temp)
        elif 21 <= bc and bc < 22:
            x['21-22'].append(temp)
        elif 22 <= bc and bc < 23:
            x['22-23'].append(temp)
        elif 23 <= bc and bc < 24:
            x['23-24'].append(temp)
        elif 24 <= bc and bc < 25:
            x['24-25'].append(temp)
        elif 25 <= bc and bc < 26:
            x['25-26'].append(temp)
        elif 26 <= bc and bc < 27:
            x['26-27'].append(temp)
        elif 27 <= bc and bc < 28:
            x['27-28'].append(temp)
        elif 28 <= bc and bc < 29:
            x['28-29'].append(temp)
        elif 29 <= bc and bc < 30:
            x['29-30'].append(temp)
        elif 30 <= bc and bc < 31:
            x['30-31'].append(temp)
        elif 31 <= bc and bc < 32:
            x['31-32'].append(temp)
        elif 32 <= bc and bc < 33:
            x['32-33'].append(temp)
        elif 33 <= bc and bc < 34:
            x['33-34'].append(temp)
        elif 34 <= bc and bc < 35:
            x['34-35'].append(temp)
        elif 35 <= bc and bc < 36:
            x['35-36'].append(temp)
        elif 36 <= bc and bc < 37:
            x['36-37'].append(temp)
        elif 37 <= bc and bc < 38:
            x['37-38'].append(temp)
        elif 38 <= bc and bc < 39:
            x['38-39'].append(temp)
        elif 39 <= bc and bc < 40:
            x['39-40'].append(temp)
        elif 40 <= bc and bc < 41:
            x['40-41'].append(temp)
        elif 41 <= bc and bc < 42:
            x['41-42'].append(temp)
        elif 42 <= bc and bc < 43:
            x['42-43'].append(temp)
        elif 43 <= bc and bc < 44:
            x['43-44'].append(temp)
        elif 44 <= bc and bc < 45:
            x['44-45'].append(temp)
        elif 45 <= bc and bc < 46:
            x['45-46'].append(temp)
        elif 46 <= bc and bc < 47:
            x['46-47'].append(temp)
        elif 47 <= bc and bc < 48:
            x['47-48'].append(temp)
        elif 48 <= bc and bc < 49:
            x['48-49'].append(temp)
        elif 49 <= bc and bc < 50:
            x['49-50'].append(temp)
        elif 50 <= bc and bc < 51:
            x['50-51'].append(temp)
        elif 51 <= bc and bc < 52:
            x['51-52'].append(temp)
        elif 52 <= bc and bc < 53:
            x['52-53'].append(temp)
        elif 53 <= bc and bc < 54:
            x['53-54'].append(temp)
        elif 54 <= bc and bc < 55:
            x['54-55'].append(temp)
        elif 55 <= bc and bc < 56:
            x['55-56'].append(temp)
        elif 56 <= bc and bc < 57:
            x['56-57'].append(temp)
        elif 57 <= bc and bc < 58:
            x['57-58'].append(temp)
        elif 58 <= bc and bc < 59:
            x['58-59'].append(temp)
        elif 59 <= bc and bc < 60:
            x['59-60'].append(temp)
        elif 60 <= bc and bc < 61:
            x['60-61'].append(temp)
        elif 61 <= bc and bc < 62:
            x['61-62'].append(temp)
        elif 62 <= bc and bc < 63:
            x['62-63'].append(temp)
        elif 63 <= bc and bc < 64:
            x['63-64'].append(temp)
        elif 64 <= bc and bc < 65:
            x['64-65'].append(temp)
        elif 65 <= bc and bc < 66:
            x['65-66'].append(temp)
        elif 66 <= bc and bc < 67:
            x['66-67'].append(temp)
        elif 67 <= bc and bc < 68:
            x['67-68'].append(temp)
        elif 68 <= bc and bc < 69:
            x['68-69'].append(temp)
        elif 69 <= bc and bc < 70:
            x['69-70'].append(temp)
        elif 70 <= bc and bc < 71:
            x['70-71'].append(temp)
        elif 71 <= bc and bc < 72:
            x['71-72'].append(temp)
        elif 72 <= bc and bc < 73:
            x['72-73'].append(temp)
        elif 73 <= bc and bc < 74:
            x['73-74'].append(temp)
        elif 74 <= bc and bc < 75:
            x['74-75'].append(temp)
        elif 75 <= bc and bc < 76:
            x['75-76'].append(temp)
        elif 76 <= bc and bc < 77:
            x['76-77'].append(temp)
        elif 77 <= bc and bc < 78:
            x['77-78'].append(temp)
        elif 78 <= bc and bc < 79:
            x['78-79'].append(temp)
        elif 79 <= bc and bc < 80:
            x['79-80'].append(temp)
        elif 80 <= bc and bc < 81:
            x['80-81'].append(temp)
        elif 81 <= bc and bc < 82:
            x['81-82'].append(temp)
        elif 82 <= bc and bc < 83:
            x['82-83'].append(temp)
        elif 83 <= bc and bc < 84:
            x['83-84'].append(temp)
        elif 84 <= bc and bc < 85:
            x['84-85'].append(temp)
        elif 85 <= bc and bc < 86:
            x['85-86'].append(temp)
        elif 86 <= bc and bc < 87:
            x['86-87'].append(temp)
        elif 87 <= bc and bc < 88:
            x['87-88'].append(temp)
        elif 88 <= bc and bc < 89:
            x['88-89'].append(temp)
        elif 89 <= bc and bc < 90:
            x['89-90'].append(temp)
        elif 90 <= bc and bc < 91:
            x['90-91'].append(temp)
        elif 91 <= bc and bc < 92:
            x['91-92'].append(temp)
        elif 92 <= bc and bc < 93:
            x['92-93'].append(temp)
        elif 93 <= bc and bc < 94:
            x['93-94'].append(temp)
        elif 94 <= bc and bc < 95:
            x['94-95'].append(temp)
        elif 95 <= bc and bc < 96:
            x['95-96'].append(temp)
        elif 96 <= bc and bc < 97:
            x['96-97'].append(temp)
        elif 97 <= bc and bc < 98:
            x['97-98'].append(temp)
        elif 98 <= bc and bc < 99:
            x['98-99'].append(temp)
        elif 99 <= bc and bc <= 100:
            x['99-100'].append(temp)
        else:
            print('here')


        # elif 21 <= bc and bc < 31:
        #     x['21-31'].append(temp)
        # elif 31 <= bc and bc < 41:
        #     x['31-41'].append(temp)
        # elif 41 <= bc and bc < 51:
        #     x['41-51'].append(temp)
        # elif 51 <= bc and bc < 61:
        #     x['51-61'].append(temp)
        # elif 61 <= bc and bc < 71:
        #     x['61-71'].append(temp)
        # elif 71 <= bc and bc < 81:
        #     x['71-81'].append(temp)
        # elif 81 <= bc and bc < 91:
        #     x['81-91'].append(temp)
        # elif 91 <= bc and bc < 101:
        #     x['91-101'].append(temp)
        # else:
        #     print('here',bc)

    return x


class get_by_symbols(generics.ListCreateAPIView):
    queryset            = by_symbols.objects.all()
    serializer_class    = BySymbolsSerialilzer

class get_cd_peformances(generics.ListAPIView):

    queryset            = cd_Peformance.objects.all()
    serializer_class    = CDPeformance

class get_trades_for_single_trade_table(generics.ListCreateAPIView):
    queryset            = TradesInChartView.objects.all()
    serializer_class    = TradesInChartViewSerializer

class peformance_serial(generics.ListCreateAPIView):
    queryset            = peformance.objects.all()
    serializer_class    = PeformanceSerializer

class get_cd_ojbects(generics.ListCreateAPIView):
    queryset            = cd_pef.objects.all()
    serializer_class    = CDPeformanceSerializer



# CREATE A CD-RANGE-PEFORMANCE OBJECT FOR EACH RANGE.
@csrf_exempt
def create_c(cdlist):

    # Clear any previous cd object data.
    cd_pef.objects.all().delete()

    # LOOP OVER EACH RANGE.
    for key, value in cdlist.items():
        
        if len(value)>0:

            active = 0
            wins = 0
            lost = 0

            lowest_price_dropped = 0
            all_price_drops = []
            lengths = []

            # LOOP OVER THE CURRENT RANGE-LIST OF TRADES.
            for trade in value:

                # Get result of current trade.
                a, w, l = utilities.get_wins_losses_active_amount(trade)
                active += a
                wins += w
                lost += l

                # Get length of current trade.
                lengths.append(trade['length']['abcd_length'])

                # If the current trade result is a 'Win', get the lowest the price dropped during the trade.
                if trade['tradeInfo']["tradeResult"] == 'Win':

                    percentage_drop, lpd = utilities.get_lowest_price_dropped_pct_on_win(trade, lowest_price_dropped)

                    all_price_drops.append(float(percentage_drop))

                    if percentage_drop > float(lowest_price_dropped):

                        lowest_price_dropped = lpd
        
            win_pct = utilities.get_win_pct(wins, lost)

            average_price_dropped = utilities.get_avg_lowest_price_dropped_on_win(wins, all_price_drops)

            total_trades = wins + lost + active

            average_length = 0

            if(len(lengths) > 0):

                average_length = '%.2f'%(statistics.mean(lengths))

            # CREATE PEFORMANCE-OBJECT FOR CURRENT RANGE PEFORMANCE.
            cd_pef.objects.create(
                bc = str(key),
                cd = key,
                trades = total_trades,
                wins = wins,
                lost = lost,
                active = active,
                win_pct = str(100)  + '%',
                lowest_price_dropped = str(lowest_price_dropped)  + '%',
                average_price_dropped = str(100) + '%',      
                rsi_wr = 0,
                volume_change_win_pct = 0,
                volume_change_lose_pct = 0,
                average_length_win = 0,
                average_length = 100,

            )

