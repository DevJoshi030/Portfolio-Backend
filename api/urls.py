from .views import GetStockData, GetStockPrice
from django.urls import path

urlpatterns = [
    path('get-stock-price/<str:stock>',
         GetStockPrice.as_view(), name='get-stock-price'),
    path('get-stock-data/<str:stock>',
         GetStockData.as_view(), name='get-stock-data'),
]
