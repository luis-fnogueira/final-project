import sys
# Appending our folder with functions
sys.path.append('functions/air/dag_functions/')

from functions.dag_functions.day_summary_dag import DaySummaryDag
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, date, timedelta


default_args = {
    'start_date': datetime(2020, 1, 1),
    'email': ['luisfalmeidanogueira@gmail.com']
}

# Creating "yesterday" object. It contains yesterday's date.
today = date.today()
yesterday = today - timedelta(days=1)

# Initializing arguments to the task function.
op_kwargs = {'year': yesterday.year, 'month': yesterday.month,
            'day': yesterday.day, 'coin': 'BTC'}

# Instatiating class
btc = DaySummaryDag()

with DAG('bitcoin', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:

    get_api = PythonOperator(
        task_id='get_api',
        python_callable=btc.getAndInputDaySummary,
        op_kwargs=op_kwargs
    )

    get_api
