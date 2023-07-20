from django.contrib import admin
from django.urls import path, include
from runScript import views

urlpatterns = [
    # path('getNasdaqCandles', views.getNasdaqCandles),
    # path('getCryptoCandles', views.getCryptoCandles),
    path('getSingleStockCandles', views.getSingleStockCandles),
    path('deleteHistory', views.deleteHistory)
]
