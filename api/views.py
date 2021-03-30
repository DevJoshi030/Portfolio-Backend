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
            return Response(data={"Error": "No Stock Found!"},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response(data={"price": price}, status=status.HTTP_200_OK)


class GetStockData(APIView):

    def get(self, request, format=None, *args, **kwargs):

        stock = kwargs['stock']
        try:
            data = si.get_data(ticker=stock, start_date="24/03/2020")
        except AssertionError:
            return Response(data={"Error": "No Stock Found!"},
                            status=status.HTTP_400_BAD_REQUEST)

        raw_data = []

        for item in data.itertuples():

            raw_data.append([
                item[0],
                str(item[1]),
                str(item[4]),
                str(item[2]),
                str(item[3]),
                str(item[6])
            ])

        return Response(data=raw_data, status=status.HTTP_200_OK)
