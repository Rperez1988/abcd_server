from django.contrib import admin
from django.urls import path, include
from CandleData import views

urlpatterns = [
    path('get_all_symbol_candles', views.get_all_symbol_candles),
    path('delete_all_candles', views.erase_candle_data),
    path('view_all_candles', views.CandleModels.as_view()),
    path('get_symbol_data', views.get_ticker_symbols),
    path('view_all_symbols', views.SymbolModels.as_view()),
    path('delete_all_symbols', views.delete_all_ticker_symbols),
    path('get_single_symbol_candles', views.get_single_symbol_candles),
    path('all_symbols_scanned', views.all_symbols_scanned),
    path('update_today_candle_data', views.update_today_candle_data),
    path('check_last_date',views.check_last_date),
    path("check_all_symbols_in_db", views.check_all_symbols_in_db),
    path('selected_candles/', views.selected_candles),
    path("view_selected_candles/", views.Selected_Candles_API.as_view()),
]
