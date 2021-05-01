from rest_framework.test import RequestsClient
from django.test import TestCase


class APITestCase(TestCase):

    def setUp(self):
        self.client = RequestsClient()
        self.url = 'https://17BCE020.pythonanywhere.com/api/'
        self.stock = 'RELIANCE.NS'

    def test_get_stock_price(self):

        response = self.client.get(self.url + 'get-stock-price/' + self.stock)
        self.assertEqual(response.status_code, 200)

    def test_get_stock_data(self):

        response = self.client.get(self.url + 'get-stock-data/' + self.stock)
        self.assertEqual(response.status_code, 200)

    def test_get_stock_stats(self):

        response = self.client.get(self.url + 'get-stock-stats/' + self.stock)
        self.assertEqual(response.status_code, 200)
