# Importing modules
from wo_airflow.db_manipulation1 import Postgres_exec
from wo_airflow.get_bitcoin1 import Bitcoin

# Instantiating Bitcoin class to get data from API and transform it to a tuple
btc = Bitcoin()

# Setting date to get from the API
response = btc.response_get(yr=2022, month=7, day=10)
print(response)

# Transforming the data receveid from the API to a tuple
normal_tuple = btc.to_tuple(response)

# Instatiating Postgres_exec class to interact with the DB
postgres = Postgres_exec()

# Inserting into the db the data obtained through the API
postgres.insert_into(normal_tuple)

# Retrieving data
postgres.select_all()