import pytest
# import requests
import datetime

from wo_airflow.db_manipulation1 import Postgres_exec

class TestPostgres_exec:
    @staticmethod
    @pytest.mark.parametrize(
        'values, expected',
        [
            (('2009-05-05', 195983.44999999, 184756.74842256, 181000, 197997.99999, '18864473.35309500', '100.91986222', 10677, 186925.27851426), None),
            ('', None),
            (('2021-01-01', 195983.44999999, 184756.74842256, 181000, 197997.99999, '18864473.35309500', '100.91986222', 10677, 186925.27851426), 1234)   
        ]
    )
    def test_insert_into(values, expected):
        db = Postgres_exec()
        actual = db.insert_into(values)   
        assert actual == expected


    """@staticmethod
    @pytest.mark.parametrize(
        'query, expected',
        [
            ('', ''),
            ('', ''),
            ('', '')
        ]
    )
    def test_select_all(query, expected):
        pass"""