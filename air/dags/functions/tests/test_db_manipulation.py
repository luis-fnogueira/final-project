from unittest.mock import patch
from functions.db_manipulation.dml_commands import DmlCommands
from functions.db_manipulation.postgres import Postgres


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

    valid_return = ("bitcoin_data", "airflow", "localhost",
                    "airflow", "5434", "public")

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
    @patch("functions.db_manipulation.postgres.Postgres", side_effect=mocked_connection)
    def test__init__(self, mocked_connection):

        expected = None

        conn = Postgres("bitcoin_data", "airflow", "localhost",
                        "airflow", "5434", "public")

        assert None is expected


class TestDmlCommands():

    def test_insert_into(self):

        data = {"date":"2022-07-24",
                "opening":123644.45861845,
                "closing":121148.14895181,
                "lowest":120784.99444257,
                "highest":126871.09910008,
                "volume":"2479581.20722043",
                "quantity":"19.94267651",
                "amount":2935,
                "avg_price":124335.42739246}

        table = "bitcoin_history"

        insert_into = DmlCommands("bitcoin_data", "airflow", "localhost",
                                  "airflow", "5434", "public")

        insert_into.insert_into(data, table)
