from airflow import DAG
#from airflow.operators.bash import BashOperator
#from airflow.operators.python import PythonOperator
#from airflow.operators.subdag import SubDagOperator
# from airflow.utils.task_group import TaskGroup
import mysql.connector
from datetime import datetime
import requests
import json


default_args = {
    'start_date': datetime(2020, 1, 1)
}


class Api_conn():
    def get_api(day: str, month: str, year: str):
        response_API = requests.get(f'https://www.mercadobitcoin.net/api/BTC/day-summary/{year}/{month}/{day}/')
        return response_API

    def load_data_json(data):
        return json.loads(data)


dia1 = Api_conn.get_api(2, 5, 2022)
load_json = Api_conn.load_data_json(dia1)
print('json_loaded')


class Mysql_conn():

    def db_conn(host, database, user, password):

        connection = mysql.connector.connect(host=host,
                                            database=database,
                                            user=user,
                                            password=password)
        cursor = connection.cursor()

        return connection, cursor


Mysql_conn.db_conn(host='172.20.0.3', database='projeto-pos', user='root', password='root' )
print('mysql connected')



with DAG('get_data', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    pass