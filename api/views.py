from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from yahoo_fin import stock_info as si


class GetStockPrice(APIView):

    def get(self, request, format=None, *args, **kwargs):

        stock = kwargs['stock']
        try:
            price = si.get_live_price(stock)
        except AssertionError:
            return Response(data={"price": None}, status=status.HTTP_200_OK)

        return Response(data={"price": price}, status=status.HTTP_200_OK)