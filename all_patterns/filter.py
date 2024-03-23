from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework import generics
from django.http import HttpResponse
from CandleData.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from .tools import *

@csrf_exempt
# FILTER: GREATER THAN / LESS THAN
def greater_than_less_than(request):


    dgt = getBodyContext(request, 'duration_gt')
    dlt = getBodyContext(request, 'duration_lt')
    egt = getBodyContext(request, 'enter_gt')
    elt = getBodyContext(request, 'enter_lt')
    status = getBodyContext(request, 'status')
    ablgt = getBodyContext(request, 'abLgt')
    abllt = getBodyContext(request, 'abLlt')
    
    if status == 'All':

        with transaction.atomic():
            current_selected_patterns = list(Pattern_ABCD.objects.filter(
                trade_entered_price__gte= egt, 
                trade_entered_price__lte=elt,
                trade_duration_bars__gte=dgt,
                trade_duration_bars__lte=dlt)
            )
            Selected_ABCD.objects.all().delete()

            for pattern in current_selected_patterns:
                create_Selected_ABCD_pattern(pattern)

    if status == 'Open':

        with transaction.atomic():
            current_selected_patterns = list(Pattern_ABCD.objects.filter(
                trade_entered_price__gte= egt, 
                trade_entered_price__lte=elt,
                trade_duration_bars__gte=dgt,
                trade_duration_bars__lte=dlt,
                pattern_AB_bar_duration__gte=ablgt,
                pattern_AB_bar_duration__lte=abllt,
                trade_is_open=True)
            )
            Selected_ABCD.objects.all().delete()

            for pattern in current_selected_patterns:
                create_Selected_ABCD_pattern(pattern)
    
    if status == 'Bull':

        with transaction.atomic():
            current_selected_patterns = list(Pattern_ABCD.objects.filter(
                trade_entered_price__gte= egt, 
                trade_entered_price__lte=elt,
                trade_duration_bars__gte=dgt,
                trade_duration_bars__lte=dlt,
                trade_result='Win')
            )
            Selected_ABCD.objects.all().delete()

            for pattern in current_selected_patterns:
                create_Selected_ABCD_pattern(pattern)
    
    if status == 'Bear':

        with transaction.atomic():
            current_selected_patterns = list(Pattern_ABCD.objects.filter(
                trade_entered_price__gte= egt, 
                trade_entered_price__lte=elt,
                trade_duration_bars__gte=dgt,
                trade_duration_bars__lte=dlt,
                trade_result="Lost")
            )
            Selected_ABCD.objects.all().delete()

            for pattern in current_selected_patterns:
                create_Selected_ABCD_pattern(pattern)
    return HttpResponse('greater_than_less_than')

