from django.contrib import admin
from django.urls import path, include
from access_trades import views

urlpatterns = [
    path('access_trades', views.get_selected_trades),
    path('access_filtered',  views.ViewTradesInChartViewSerializer.as_view()),
    path('access_peformance', views.peformance_serial.as_view()),
    path('get_trades_of_selected_symbol', views.get_trades_of_selected_symbol),

  
]
