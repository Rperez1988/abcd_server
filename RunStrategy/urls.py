from django.contrib import admin
from django.urls import path, include
from RunStrategy import views

urlpatterns = [
    path('scan_single_symbols', views.scan_single_symbols),
    path('scan_all_symbols', views.scan_all_symbols),
    path('duplicates', views.remove_duplicate_entries)
    
]
