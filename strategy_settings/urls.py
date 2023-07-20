from django.urls import path
from strategy_settings import views

urlpatterns = [
    path('get', views.strategySettingsModels.as_view()),
    path('save', views.saveStrategySettings),
    path('view', views.strategySettingsModels.as_view()),
    path('delete', views.deleteSettings),
    path('edit', views.editSingularSetting),
    path('updateSelectedSetting', views.updateSelectedSetting),
    path('updateAndSave', views.update_and_save)

]
