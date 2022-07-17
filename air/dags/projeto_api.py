from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, date, timedelta
import sys


# Appending our folder with functions
sys.path.append('air/dags/functions')
from functions.dag_functions import DaySummaryDag


# Defining default_args as 2020/01/01
default_args = {
    'start_date': datetime(2020, 1, 1)
}

# Creating yesterday's object.
today = date.today()
yesterday = today - timedelta(days = 1)

# Instatiating class
btc = DaySummaryDag()

with DAG('bitcoin', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    

    get_api = PythonOperator(
        task_id='get_api',
        python_callable=btc.getAndInputDaySummary,
        op_kwargs={'year': yesterday.year, 'month': yesterday.month, 'day': yesterday.day, 'coin': 'BTC'}
        )


    get_api
