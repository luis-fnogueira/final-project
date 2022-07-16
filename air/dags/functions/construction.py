import json
import psycopg2
import requests
import re


class Postgres():

    # Constructor method initializing the connection to DB and creating cursor
    def __init__(self, db, user, host, password, port):
        
        self.db = db
        self.user = user
        self.host = host
        self.password = password
        self.port = port

        self.conn = psycopg2.connect(
            database=db, host=host, port=port, password=password, user=user)
        self.cur = self.conn.cursor()

    # SQL INSERT INTO method.
    def insert_into(self, columns, values, table):

        postgres_insert_query = f"""INSERT INTO {self.db}.{table} {tuple(columns)} VALUES {tuple(values)}"""

        print(postgres_insert_query)
        yield self.cur.query(postgres_insert_query)
        self.conn.commit()



class Bitcoin():

    # This function gets data from API 
    def response_get(self, year: int, month: int, day: int):

        URL = 'https://www.mercadobitcoin.net/api/BTC/day-summary'

        response_API = requests.get(f'{URL}/{year}/{month}/{day}')
        
        to_json = response_API.json()

        values =  []

        columns = []

        for column, value in to_json.items():
            values.append(value)
            columns.append(column)

        #columns = json.dumps(columns)
        #values = json.dumps(values)        


        return columns, values

if __name__ == '__main__':
    postgres = Postgres(db="bitcoin_data", user="airflow", host="localhost",
                        password="airflow", port="5434")

    bitcoin = Bitcoin()

    response = bitcoin.response_get(2022, 7, 14)

    #print(response[0], response[1])

    table = 'bitcoin_history'

    postgres.insert_into(columns=response[0], values=response[1], table=table)

    #postgres.insert_into(response[0], response[1], table)

    #print(len(response[1]))