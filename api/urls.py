from .views import GetStockPrice
from django.urls import path

urlpatterns = [
    path('get-stock-price/<str:stock>',
         GetStockPrice.as_view(), name='get-stock-price'),
]
