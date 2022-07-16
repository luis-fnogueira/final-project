from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, date, timedelta
import sys

# Appending our folder with functions
sys.path.append('air/dags/functions')

from functions.db_manipulation import Database
from functions.get_bitcoin import Bitcoin


# Defining default_args as 2020/01/01
default_args = {
    'start_date': datetime(2020, 1, 1)
}

# Creating yesterday's object.
today = date.today()
yesterday = today - timedelta(days = 1)

# Instatiating classes from Bitcoin and Database
btc = Bitcoin()
db = Database()


with DAG('bitcoin', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    
    get_api = PythonOperator(
        task_id='get_api',
        python_callable=btc.response_get,
        op_kwargs={'yr': yesterday.year, 'month': yesterday.month, 'day': yesterday.day}
        )


    parse_tuple = PythonOperator(
        task_id='parse_tuple',
        python_callable=btc.to_tuple,
    )


    insert_into = PythonOperator(
        task_id='insert_into',
        python_callable=db.insert_into
    )

    get_api >> parse_tuple >> insert_into
