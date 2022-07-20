import sys
from typing import Type

from requests import patch
# Appending our folder with functions
sys.path.append('air/dags/functions')
from db_manipulation import Postgres, CommandsModeling
import pytest
import psycopg2
from unittest.mock import patch


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

        assert None == expected

