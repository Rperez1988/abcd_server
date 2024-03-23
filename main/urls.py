
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('runScript.urls')),
    path('all_patterns_info/', include('all_patterns_info.urls')),
    path('patterns/', include('all_patterns.urls')),
    path('run_strategy/', include('RunStrategy.urls')),
    path('candle_data/', include('CandleData.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
