import pytest
# import requests
import datetime

from get_bitcoin import Bitcoin


class TestDaySummaryApi:
    @staticmethod
    @pytest.mark.parametrize(
        'date, expected',
        [
            (datetime.date(2022, 5, 5), '{"date":"2022-05-05","opening":195983.44999999,"closing":184756.74842256,"lowest":181000,"highest":197997.99999,"volume":"18864473.35309500","quantity":"100.91986222","amount":10677,"avg_price":186925.27851426}'),
            (datetime.date(2022, 4, 5), '{"date":"2022-05-05","opening":195983.44999999,"closing":184756.74842256,"lowest":181000,"highest":197997.99999,"volume":"18864473.35309500","quantity":"100.91986222","amount":10677,"avg_price":186925.27851426}'),
            (datetime.date(2022, 3, 5), '{"date":"2022-05-05","opening":195983.44999999,"closing":184756.74842256,"lowest":181000,"highest":197997.99999,"volume":"18864473.35309500","quantity":"100.91986222","amount":10677,"avg_price":186925.27851426}')   
        ]
    )
    def test_get_bitcoin(date, expected):
        response_API = Bitcoin()
        actual = response_API.response_get(
            day=date.day,
            month=date.month,
            yr=date.year)   
        assert actual == expected


    
    @staticmethod
    @pytest.mark.parametrize(
        'data, expected',
        [
            (str({"date":"2022-05-05","opening":195983.44999999,"closing":184756.74842256,"lowest":181000,"highest":197997.99999,"volume":"18864473.35309500","quantity":"100.91986222","amount":10677,"avg_price":186925.27851426}), ('2022-05-05', 195983.44999999, 184756.74842256, 181000, 197997.99999, '18864473.35309500', '100.91986222', 10677, 186925.27851426)),
            ({"date":"2022-05-05","opening":195983.44999999,"closing":184756.74842256,"lowest":181000,"highest":197997.99999,"volume":"18864473.35309500","quantity":"100.91986222","amount":10677,"avg_price":186925.27851426}, ('2022-05-05', 195983.44999999, 184756.74842256, 181000, 197997.99999, '18864473.35309500', '100.91986222', 10677, 186925.27851426)),
            (str({"date":"2002-05-05","opening":195983.44999999,"closing":184756.74842256,"lowest":181000,"highest":197997.99999,"volume":"18864473.35309500","quantity":"100.91986222","amount":10677,"avg_price":186925.27851426}), ('2022-05-05', 195983.44999999, 184756.74842256, 181000, 197997.99999, '18864473.35309500', '100.91986222', 10677, 186925.27851426))
        ]
    )
    def test_to_tuple(data, expected):
        btc = Bitcoin()
        actual = btc.to_tuple(data)  
        assert actual == expected