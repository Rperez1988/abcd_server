
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('runScript.urls')),
    path('', include('runScript.urls')),
    path('stats/', include('total_statistics.urls')),
    path('trade/', include('trade.urls')),
    path('settings/', include('strategy_settings.urls')),
    path('api/traderesults', include('stock.urls')),
    path('api/totalresults', include('stock.urls')),
    path('api/stocksTested', include('stock.urls')),
    path('api/savedLists', include('stock.urls')),
    path('api/chartImage', include('stock.urls')),
    path('api/activeTrades', include('stock.urls')),
    path('access_trades/', include('access_trades.urls')),
  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
