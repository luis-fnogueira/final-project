from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, date, timedelta
from get_bitcoin import Bitcoin


default_args = {
    'start_date': datetime(2020, 1, 1)
}

today = date.today()
yesterday = today - timedelta(days = 1)

btc = Bitcoin()


with DAG('bitcoin_input', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    
    get_api = PythonOperator(
        task_id='get_api',
        python_callable=btc.response_get(yr=yesterday.year, month=yesterday.month, day=yesterday.day)
    )

