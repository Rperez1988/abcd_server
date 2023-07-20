from django.urls import path
from total_statistics import views

urlpatterns = [
    path('createStatistics', views.createStatistics),
    path('access_all_statistics_models', views.statisticsModels.as_view()),
    
]
