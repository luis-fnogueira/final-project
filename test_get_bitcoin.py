import decimal
import pytest
# import requests
import datetime

from get_bitcoin import Bitcoin


class TestDaySummaryApi:
    @staticmethod
    @pytest.mark.parametrize(
        'date, expected',
        [
            (datetime.date(2021, 6, 21), str({"date":"2021-06-21","opening":182018.62236,"closing":167597.94809,"lowest":158000,"highest":182018.62236,"volume":"47640150.72831583","quantity":"286.48516078","amount":19363,"avg_price":166291.86167481}))
        ]
    )
    def test_get_bitcoin(date, expected):
        actual = Bitcoin.response_get(
            day=date.day,
            month=date.month,
            year=date.year)   
        assert actual == expected


    
    @staticmethod
    @pytest.mark.parametrize(
        'data, expected',
        [
            (str({"date":"2021-06-21","opening":182018.62236,"closing":167597.94809,"lowest":158000,"highest":182018.62236,"volume":"47640150.72831583","quantity":"286.48516078","amount":19363,"avg_price":166291.86167481}), {'date': '2021-06-21', 'opening': 182018.62236, 'closing': 167597.94809, 'lowest': 158000, 'highest': 182018.62236, 'volume': '47640150.72831583', 'quantity': '286.48516078', 'amount': 19363, 'avg_price': 166291.86167481})
        ]
    )
    def test_to_json(data, expected):
        actual = Bitcoin.to_json(data)  
        assert actual == expected