from django.contrib import admin
from django.urls import path, include
from access_trades import views

urlpatterns = [
    
    # GATHER ALL TRADES OF SELECTED SYMBOL
    path('get_all_trades_of_selected_symbol', views.get_all_trades_of_selected_symbol),
    
    
    path('create_trades_for_single_trade_table', views.create_trades_for_single_trade_table),
    path('get_trades_for_single_trade_table',  views.get_trades_for_single_trade_table.as_view()),



    path('access_peformance', views.peformance_serial.as_view()),
    path('get_trades_of_selected_symbol', views.get_trades_of_selected_symbol),


    path('create_cd_objects', views.create_cd_peformances),
    path('get_cd_ojbects', views.get_cd_ojbects.as_view()),

    # path('create_cd_peformances', views.create_cd_peformances),
    path('get_cd_peformances', views.get_cd_peformances.as_view()),


    path('create_by_symbol_object', views.create_by_symbol_object),
    path('get_by_symbols', views.get_by_symbols.as_view())
  
]
