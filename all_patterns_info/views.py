from django.shortcuts import render
from all_patterns.models import *
from all_patterns_info.models import All_Patterns_Info
from django.http import HttpResponse
from all_patterns_info.tools import *
from django.views.decorators.csrf import csrf_exempt
from all_patterns.views import *

def getBodyContext(request, str):

    body_unicode = request.body.decode('utf-8')
    
    import ast
    d = ast.literal_eval(body_unicode)


    return (d[str])

@csrf_exempt
def get_selected_symbol(request):

    trade_ids = getBodyContext(request,'trade_ids')
    selected_patterns(trade_ids)
    
    return HttpResponse('get_selected_symbol')

def add_symbol_ALL(request):

    patterns = list(Pattern_ABCD.objects.all())

    abcds = []
    open_abcds = []
    passed_abcds = []
    failed_abcds = []
    abcd_lengths = []
    c_retracements = []

    for pattern in patterns:

        # ABCD COUNT
        abcds.append(pattern)
        # OPEN, PASSED, FAILED COUNT
        if pattern.trade_result == 'Win':
            passed_abcds.append(pattern)
        elif pattern.trade_result == 'Lost':
            failed_abcds.append(pattern)
        elif pattern.trade_is_open == True:
            open_abcds.append(pattern)
        # ABCD lENGTH COUNT
        abcd_lengths.append(pattern.pattern_ABCD_bar_length)
        # C RETRACEMENT
        c_retracements.append(pattern.pattern_C_price_retracement)

         # PASSED_PCT
        passed_pct = symbol_passed_pct(len(abcds), passed_abcds, failed_abcds)

    abcd = All_Patterns_Info.objects.create(
        symbol = 'All Symbols',
        total_abcds = len(abcds),
        passed_abcds = len(passed_abcds),
        failed_abcds = len(failed_abcds),
        open_abcds = len(open_abcds),
        passed_pct = passed_pct,
    )

    abcd.abcd_instances.add(*abcds)

    return HttpResponse('all')

def delete_all_info(request):
    All_Patterns_Info.objects.all().delete()
    return HttpResponse('create all info')

def create_all_info(request):

    # GATHER ALL SYMBOLS
    all_symbols = list(Pattern_ABCD.objects.values('trade_symbol').distinct())
    
    # GET EACH SYMBOL INFO
    for symbol in all_symbols:
        
        # GET EACH PATTERN FOR CURRENT SYMBOL
        patterns = list(Pattern_ABCD.objects.filter(trade_symbol=symbol['trade_symbol']))

        abcds = []
        open_abcds = []
        passed_abcds = []
        failed_abcds = []
        abcd_lengths = []
        c_retracements = []

        avg_low_c_retracement = 0
        price_drops = []
        avg_low_pd = 0

        for pattern in patterns:

            # ABCD COUNT
            abcds.append(pattern)
            # OPEN, PASSED, FAILED COUNT
            if pattern.trade_result == 'Win':
                passed_abcds.append(pattern)
            elif pattern.trade_result == 'Lost':
                failed_abcds.append(pattern)
            elif pattern.trade_is_open == True:
                open_abcds.append(pattern)
            # ABCD lENGTH COUNT
            abcd_lengths.append(pattern.pattern_ABCD_bar_length)
            # C RETRACEMENT
            c_retracements.append(pattern.pattern_C_price_retracement)
        
        # PASSED_PCT
        passed_pct = symbol_passed_pct(len(abcds), passed_abcds, failed_abcds)

        abcd = All_Patterns_Info.objects.create(
            symbol = symbol['trade_symbol'],
            total_abcds = len(abcds),
            passed_abcds = len(passed_abcds),
            failed_abcds = len(failed_abcds),
            open_abcds = len(open_abcds),
            passed_pct = passed_pct,
        )

        abcd.abcd_instances.add(*abcds)

        print(symbol['trade_symbol'])
        print('Patterns:', len(patterns))
        print('Passed_Pct', passed_pct)
        print('passed_abcds:', len(passed_abcds))
        print('failed_abcds:', len(failed_abcds))
        print('open_abcds:', len(open_abcds))
        

    return HttpResponse('create all info')