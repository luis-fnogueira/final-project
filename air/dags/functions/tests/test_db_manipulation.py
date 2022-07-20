import sys
# Appending our folder with functions
sys.path.append('air/dags/functions')
from db_manipulation import Postgres, CommandsModeling
import pytest
import psycopg2


@pytest.fixture()
def fixture_db_conn():
    return "SELECT 'amount' FROM public.bitcoin_history WHERE 'amount' = %s"


class TestClassPostgres():

    
    @pytest.mark.parametrize(
    "db, user, host, password, port, schema, expected",
        [
        ("bitcoin_data", "airflow", "localhost", "airflow", "5434",
        "public", 2602)
        ]
    )
    def test__init__(self, db, user, host, password, port, schema, expected, 
                    fixture_db_conn):
        

        conn = Postgres(db=db, user=user, host=host, password=password, port=
                        port, schema=schema)

        conn.cur.execute(fixture_db_conn, (2602,))
        actual = conn.cur.fetchall()

        assert actual == expected

