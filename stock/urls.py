from django.contrib import admin
from django.urls import path, include
from runScript import views
from . import views

urlpatterns = [
    # path('', views.AllModels.as_view()),
    
    path('', views.AllModels.as_view()),
    path('api/traderesults', views.tradeResultModels.as_view()),
    path('api/totalresults', views.totalResultsModels.as_view()),
    path('api/stocksTested', views.stocksTestedModels.as_view()),
    path('api/savedLists', views.savedListsTestedModels.as_view()),
    path('api/chartImage', views.chartImageModels.as_view()),
    path('api/stockStatistics', views.stockStatisticsModels.as_view()),
    path('api/activeTrades', views.activeTradesModels.as_view()),
    path('<int:pk>/', views.SingleModel.as_view()),
    path('singleStockEngine', views.singleStockEngine),
    path('getStockStatistics', views.getStockStatistics),
    path('newSavedList', views.newSavedList),
    path('CSVtoDatabase', views.CSVtoDatabase),
    path('deleteSavedList', views.deleteSavedList),
    path('deleteItemsInList', views.deleteItemsInList),
    path('getTradeID', views.getTradeID),
    path('deleteChartImage', views.deleteChartImage),
    path('getLiveData', views.getLiveData),
]
