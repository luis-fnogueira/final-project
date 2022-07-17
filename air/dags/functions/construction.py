import json
import psycopg2
import requests
from sqlalchemy import values



class Postgres():

    # Constructor method initializing the connection to DB and creating cursor
    def __init__(self, db, user, host, password, port, schema):
        
        self.db = db
        self.user = user
        self.host = host
        self.password = password
        self.port = port
        self.schema = schema

        self.conn = psycopg2.connect(
            database=db, host=host, port=port, password=password, user=user)
        self.cur = self.conn.cursor()

    # SQL INSERT INTO method.
    def insert_into(self, data, table):

        values = tuple(data.values())

        numberOfColumnsMinusOne = len(values) - 1
        valuesParametersMinusOne = '%s, ' * numberOfColumnsMinusOne

        postgres_insert_query = f"INSERT INTO {self.schema}.{table} VALUES ({valuesParametersMinusOne}%s)  "

        print(postgres_insert_query)

        self.cur.execute(postgres_insert_query, values)

        self.conn.commit()
        


class Bitcoin():

    # This function gets data from API 
    def response_get(self, year: int, month: int, day: int):

        URL = 'https://www.mercadobitcoin.net/api/BTC/day-summary'

        ApiResponse = requests.get(f'{URL}/{year}/{month}/{day}')
        
        to_json = ApiResponse.json()
        
        return to_json

if __name__ == '__main__':
    postgres = Postgres(db="bitcoin_data", user="airflow", host="localhost",
                        password="airflow", port="5434", schema='public')

    bitcoin = Bitcoin()

    response = bitcoin.response_get(2022, 7, 14)

    table = 'bitcoin_history'

    postgres.insert_into(response, table=table)
