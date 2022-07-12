from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, date, timedelta
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator

from get_bitcoin import Bitcoin


default_args = {
    'start_date': datetime(2020, 1, 1)
}

today = date.today()
yesterday = today - timedelta(days = 1)

btc = Bitcoin()


with DAG('bitcoin', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    
    """get_api = SimpleHttpOperator(
        task_id='get_api',
        http_conn_id='btc_get',
        endpoint=f'/{yesterday.year}/{yesterday.month}/10',
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )"""

    get_api = PythonOperator(
        task_id='get_api',
        python_callable=btc.response_get,
        op_kwargs={'yr': 2022, 'month': 7, 'day': 10}
        #op_kwargs={'yr': yesterday.year, 'month': yesterday.month, 'day': yesterday.day}
        )


    parse_tuple = PythonOperator(
        task_id='parse_tuple',
        python_callable=btc.to_tuple,
    )

    get_api >> parse_tuple
