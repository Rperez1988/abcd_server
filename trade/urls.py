from django.urls import path
from trade import views

urlpatterns = [
    path('access_all_trade_models', views.tradeModels.as_view()),
    path('incrementTradesInView', views.incrementTradesInView.as_view()),
    
]
