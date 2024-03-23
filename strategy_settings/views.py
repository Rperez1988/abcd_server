from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import StrategySettingsSerializer
from .models import strategySettings
from stock.ultilities import *
import json
from django.http import JsonResponse

@csrf_exempt
def deleteSettings(request):

    id = getBodyContext(request ,'id')
    last_id = getBodyContext(request, 'last_id')
    strategySettings.objects.filter(id=id).delete()
    last_setting = strategySettings.objects.get(id=last_id)
    last_setting.isSelected = "true"
    last_setting.save()
    
    return HttpResponse('deleteSettings')

@csrf_exempt
def editSingularSetting(request):



    old_name = getBodyContext(request ,'settingsName')
    new_name= getBodyContext(request ,'newName')
    # setting_name = strategySettings.objects.get(settingsName=old_name)
    # setting_name.settingsName = new_name
    # setting_name.save()

    strategySettings.objects.filter(settingsName=old_name).update(settingsName=new_name, isSelected='true')
    

    # name = getBodyContext(request ,'settingsName')
    # newName = getBodyContext(request ,'newName')
    # market = getBodyContext(request, 'market')
    # pivotLength = getBodyContext(request, 'pivotLength')
    # rrr = getBodyContext(request, 'rrr')
    # sAndr = getBodyContext(request, 'sAndr')
    # maxAtoBLength = getBodyContext(request, 'maxAtoBLength')
    # maxBtoCLength = getBodyContext(request, 'maxBtoCLength')
    # maxCtoDLength = getBodyContext(request, 'maxCtoDLength')
    # entryRSI = getBodyContext(request, 'entryRSI')
    # abnormalPriceJump = getBodyContext(request, 'abnormalPriceJump')
    # pivotSteepness = getBodyContext(request, 'pivotSteepness')
    # aBelowB = getBodyContext(request, 'aBelowB')
    # isComplete = getBodyContext(request, 'isComplete')
 


    # settingID = strategySettings.objects.get(settingsName=name)
    # setting = strategySettings.objects.get(id = settingID.id)

    # strategySettings.objects.filter(pk=settingID.id).update(settingsName=newName)
    # strategySettings.objects.filter(pk=settingID.id).update(market=market)
    # strategySettings.objects.filter(pk=settingID.id).update(pivotLength=pivotLength)
    # strategySettings.objects.filter(pk=settingID.id).update(rrr=rrr)
    # strategySettings.objects.filter(pk=settingID.id).update(sAndr=sAndr)
    # strategySettings.objects.filter(pk=settingID.id).update(maxAtoBLength=maxAtoBLength)
    # strategySettings.objects.filter(pk=settingID.id).update(maxBtoCLength=maxBtoCLength)
    # strategySettings.objects.filter(pk=settingID.id).update(maxCtoDLength=maxCtoDLength)
    # strategySettings.objects.filter(pk=settingID.id).update(entryRSI=entryRSI)
    # strategySettings.objects.filter(pk=settingID.id).update(abnormalPriceJump=abnormalPriceJump)
    # strategySettings.objects.filter(pk=settingID.id).update(pivotSteepness=pivotSteepness)
    # strategySettings.objects.filter(pk=settingID.id).update(aBelowB=aBelowB)
    # strategySettings.objects.filter(pk=settingID.id).update(isComplete=isComplete)

    return  HttpResponse('editSetting')

@csrf_exempt
def getStrategySettings(request):

    return HttpResponse('getStrategySettings')

@csrf_exempt
def editSetting(request):

    return HttpResponse()

@csrf_exempt
def update_and_save(request):





    # Parse the JSON data in the request body into a Python dictionary
    request_data = json.loads(request.body)


    # Access the values in the dictionary
    symbol = request_data.get('symbol')
    id = request_data.get('id')
    settings_name = request_data.get('settingsName')
    market = request_data.get('market')
    pivot_length = request_data.get('pivotLength')
    rrr = request_data.get('rrr')
    s_and_r = request_data.get('sAndr')
    max_ato_b_length = request_data.get('maxAtoBLength')
    max_bto_c_length = request_data.get('maxBtoCLength')
    max_cto_d_length = request_data.get('maxCtoDLength')
    entry_rsi = request_data.get('entryRSI')
    abnormal_price_jump = request_data.get('abnormalPriceJump')
    pivot_steepness = request_data.get('pivotSteepness')
    a_below_b = request_data.get('aBelowB')
    is_selected = request_data.get('isSelected')
    is_complete = request_data.get('isComplete')
    startDate = request_data.get('startDate')
    endDate = request_data.get('endDate')

    setting = strategySettings.objects.get(id=id)
    setting.symbol = symbol
    setting.isSelected = "true"
    setting.save()
    setting.settingsName = settings_name
    setting.market = market
    setting.pivotLength = pivot_length
    setting.rrr = rrr
    setting.sAndr = s_and_r
    setting.maxAtoBLength = max_ato_b_length
    setting.maxBtoCLength = max_bto_c_length
    setting.maxCtoDLength = max_cto_d_length
    setting.entryRSI = entry_rsi
    setting.abnormalPriceJump = abnormal_price_jump
    setting.pivotSteepness =pivot_steepness
    setting.aBelowB = a_below_b
    setting.isComplete = is_complete
    setting.isSelected =is_selected
    setting.startDate = startDate
    setting.endDate = endDate

    setting.save()
        
    return HttpResponse('deleteSettings')

@csrf_exempt
def saveStrategySettings(request):

    # Get all objects in the model
    objects = strategySettings.objects.all()

    # Loop through each object and set the key to false
    for obj in objects:
        obj.isSelected = 'false'
        obj.save()

    strategySettings.objects.get_or_create(

        settingsName = getBodyContext(request, 'settingsName'),
        market = getBodyContext(request, 'market'),
        pivotLength = getBodyContext(request, 'pivotLength'),
        rrr = getBodyContext(request, 'rrr'),
        sAndr = getBodyContext(request, 'sAndr'),
        maxAtoBLength = getBodyContext(request, 'maxAtoBLength'),
        maxBtoCLength = getBodyContext(request, 'maxBtoCLength'),
        maxCtoDLength = getBodyContext(request, 'maxCtoDLength'),
        entryRSI = getBodyContext(request, 'entryRSI'),
        abnormalPriceJump = getBodyContext(request, 'abnormalPriceJump'),
        pivotSteepness = getBodyContext(request, 'pivotSteepness'),
        aBelowB = getBodyContext(request, 'aBelowB'),
        startDate = getBodyContext(request, 'startDate'),
        endDate = getBodyContext(request, 'endDate'),
        isComplete = 'false',
        isSelected = 'true'
        
    )
    

    return HttpResponse('saveStrategySettings')

@csrf_exempt
def updateSelectedSetting(request):

    previous_id = getBodyContext(request ,'previousID')
    new_id = getBodyContext(request , 'newID')

    previous_id = strategySettings.objects.get(id=previous_id)
    previous_id.isSelected = "false"
    previous_id.save()

    new_id = strategySettings.objects.get(id=new_id)
    new_id.isSelected = "true"
    new_id.save()


    return HttpResponse('saveStrategySettings')

@csrf_exempt
def setLastItemToTrue(request):
    return


class strategySettingsModels(generics.ListCreateAPIView):
    queryset            = strategySettings.objects.all()
    serializer_class    = StrategySettingsSerializer

    def post(self, request, *args, **kwargs):
        # Access the request object
        print(request.data)  # This will print the POST data
