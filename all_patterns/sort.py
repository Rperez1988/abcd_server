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
def sort_greater_than_less_than(request):

    with transaction.atomic():

        current_selected_patterns = list(Selected_ABCD.objects.order_by('trade_entered_price'))
        Selected_ABCD.objects.all().delete()
        for pattern in current_selected_patterns:
            create_Selected_ABCD_pattern(pattern)
    return HttpResponse('sort')
