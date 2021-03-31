from .views import GetStockData, GetStockPrice, GetStockStat
from django.urls import path

urlpatterns = [
    path('get-stock-price/<str:stock>',
         GetStockPrice.as_view(), name='get-stock-price'),
    path('get-stock-data/<str:stock>',
         GetStockData.as_view(), name='get-stock-data'),
    path('get-stock-stats/<str:stock>',
         GetStockStat.as_view(), name='get-stock-stat'),
]
