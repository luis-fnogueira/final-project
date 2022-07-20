import sys
# Appending our folder with functions
sys.path.append('air/dags/functions')
from db_manipulation import Postgres, CommandsModeling
import pytest
import psycopg2


@pytest.fixture()
def fixture_db_conn():
    return "SELECT date FROM public.bitcoin_history WHERE date = '2022-07-10"


class TestClassPostgres():

    
    @pytest.mark.parametrize(
    "db, user, host, password, port, schema, expected",
        [
        ("bitcoin_data", "airflow", "localhost", "airflow", "5434",
        "public", "2022-07-10")
        ]
    )
    def test__init__(self, db, user, host, password, port, schema, expected):
        

        conn = Postgres(db=db, user=user, host=host, password=password, port=
        port, schema=schema)

        actual = conn.cur.execute(fixture_db_conn)

        assert actual == expected

