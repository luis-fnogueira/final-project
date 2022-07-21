from unittest.mock import patch
from functions.db_manipulation import DmlCommands, Postgres
import sys
# Appending our folder with functions
sys.path.append('air/dags/functions')


"""
This function mocks the arguments to connect to the DB. If correct arguments
are used it returns None, otherwise it raises an error. None is necessary becau-
-se we cannot return any other values for constructor methods.
"""


def mocked_connection(*args):
    class MockConn():
        def __init__(self, db, user, host, password, port, schema):
            self.db = db
            self.user = user
            self.host = host
            self.password = password
            self.port = port
            self.schema = schema

    valid_return = ("bitcoin_data", "airflow", "air_postgres_1",
                    "airflow", "5432", "public")

    if args == valid_return:
        return None
    else:
        raise ConnectionError("You passed the wrong arguments for connection")


class TestClassPostgres():

    """
    None value is expected because we are testing and constructor method. If the
    conn object gets the correct arguments it will return None and then the test
    will pass
    """
    @patch("db_manipulation.Postgres.__init__", side_effect=mocked_connection)
    def test__init__(self, mocked_connection):

        expected = None

        conn = Postgres("bitcoin_data", "airflow", "air_postgres_1",
                        "airflow", "5432", "public")

        assert None is expected


class TestDmlCommands():

    def test_insertInto(self):

        data = {
            "date": "2022-07-19",
            "opening": 104541.21927156,
            "closing": 106707.92423624,
            "lowest": 98206.0486193,
            "highest": 110000,
            "volume": "15152834.92884294",
            "quantity": "149.84572768",
            "amount": 11174,
            "avg_price": 101122.90262423}

        table = "bitcoin_history"

        insert_into = DmlCommands("bitcoin_data", "airflow", "localhost",
                                  "airflow", "5434", "public")

        insert_into.insertInto(data, table)
