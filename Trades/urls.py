from django.urls import path, include
from Trades import views

urlpatterns = [
    path('view', views.TradeSerializer.as_view()),
    path('view', views.delete),
    path('view_single_a_pivots', views.SinglePivotSerializer.as_view()),
]