from django.contrib import admin
from django.urls import path, include
from runScript import views
from . import views
from .filter import *
from .sort import *

urlpatterns = [
    # path('', views.AllModels.as_view()),

    path('a_patterns/', views.A_Patterns_Serializer.as_view()),
    path('ab_patterns/', views.AB_Patterns_Serializer.as_view()),
    path('abc_patterns/', views.ABC_Patterns_Serializer.as_view()),
    path('abcd_patterns/', views.Patterns_Serializer.as_view()),
    path('selected_abcd/', views.Selected_ABCD_Serializer.as_view()),
    
    path('check_symbols_ran/', views.check_symbols_ran),

    path("sort_selected/",views.sort_selected),

    path('update_count/', views.update_patterns_list_count),
    path('gtlt/', greater_than_less_than),
    path('sort_gtlt/', sort_greater_than_less_than),

    path('delete_all_patterns', views.delete_all_patterns)
]
 