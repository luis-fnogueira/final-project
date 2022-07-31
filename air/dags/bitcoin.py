from airflow import DAG
from datetime import datetime, date, timedelta
from airflow.operators.python import PythonOperator
from functions.dag_functions.day_summary_dag import DaySummaryDag


DOC_MD = """
### DAG
### Purpose
This dag gets data from Mercado Bitcoin API and inputs into a database. The data
are fetched daily. The API only makes available historical data i.e., it doesn't show
current day's data.
"""


DEFAULT_ARGS = {
    'start_date': datetime(2020, 1, 1),
    'email': ['luisfalmeidanogueira@gmail.com']
}

# Yesterday's date.
TODAY = date.today()
YESTERDAY = TODAY - timedelta(days=1)

# Initializing arguments to the task function.
op_kwargs = {
    'year': YESTERDAY.year, 
    'month': YESTERDAY.month,
    'day': YESTERDAY.day,
    'coin': 'BTC'
}

# Instatiating class to use get_and_input_day_summary method
btc = DaySummaryDag()

with DAG(
    dag_id='bitcoin',
    schedule_interval='@daily',
    default_args=DEFAULT_ARGS,
    catchup=False,
    doc_md=DOC_MD
) as dag:

    get_api = PythonOperator(
        task_id='get_api',
        python_callable=btc.get_and_input_day_summary,
        op_kwargs=op_kwargs
    )

    get_api
