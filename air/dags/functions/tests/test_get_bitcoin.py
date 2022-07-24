from functions.get_bitcoin.mercado_bitcoin import GetResponse, MercadoBitcoin
import pytest
from unittest.mock import patch
from unittest import TestCase
import requests


"""
This is function that mocks the response from the API. If the value passed is valid
it returns 200 and a set {"foo": "bar"}, otherwise it returns an error and no JSON
"""


def mocked_requests_get(*args, **kwargs):
    class MockResponse(requests.Response):
        def __init__(self, json_data, status_code):
            super().__init__()
            self.status_code = status_code
            self.json_data = json_data

        def json(self):
            return self.json_data

        def raise_for_status(self) -> None:
            if self.status_code != 200:
                raise Exception

    if args[0] == "valid_endpoint":
        return MockResponse(json_data={"foo": "bar"}, status_code=200)
    else:
        return MockResponse(json_data=None, status_code=404)


class TestGetResponse(TestCase):

    @patch("get_bitcoin.GetResponse.getDeserialize",
           side_effect=mocked_requests_get)
    def testGetDeserialize(self, mock_getDeserialize):

        expected = {'foo': 'bar'}

        get_response = GetResponse()
        response = get_response.getDeserialize("valid_endpoint")

        response_json = response.json()

        assert response_json == expected


class TestMercadoBitcoin():

    @pytest.mark.parametrize("coin, method, expected",
                             [("BTC",
                               "ticker",
                               "https://www.mercadobitcoin.net/api/BTC/ticker/"),
                              ("ETH",
                               "ticker",
                                 "https://www.mercadobitcoin.net/api/ETH/ticker/")])
    def test_standardGet(self, coin, method, expected):

        actual = MercadoBitcoin()
        actual.standardGet(coin=coin, method=method)
        assert actual.URL == expected

    @pytest.mark.parametrize("year, month, day, coin, expected",
                             [(2022,
                               7,
                               15,
                               "BTC",
                               "https://www.mercadobitcoin.net/api/BTC/day-summary/2022/7/15"),
                              (2022,
                               7,
                               10,
                               "BTC",
                                 "https://www.mercadobitcoin.net/api/BTC/day-summary/2022/7/10")])
    def test_daySummary(self, year, month, day, coin, expected):
        actual = MercadoBitcoin()
        actual.daySummary(year, month, day, coin)
        assert actual.URL == expected
