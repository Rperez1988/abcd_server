


from django.contrib import admin
from django.urls import path, include
from runScript import views
from . import views, models

urlpatterns = [
    # path('', views.AllModels.as_view()),

    path('create_all_info/', views.create_all_info),
    path('view_all_info/', models.All_Patterns_Serializer.as_view()),
    path('delete/', views.delete_all_info),
    path("get_selected_symbol/", views.get_selected_symbol),
    path("create_ALL/", views.add_symbol_ALL)

]
