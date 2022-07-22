# Appending our folder with air
import sys
sys.path.append('/air/dags/functions/')


from functions.get_bitcoin.mercado_bitcoin import MercadoBitcoin
from functions.db_manipulation.dml_commands import DmlCommands


class DaySummaryDag():

    def getAndInputDaySummary(
            self,
            year: int,
            month: int,
            day: int,
            coin: int):

        bitcoin = MercadoBitcoin()
        response = bitcoin.daySummary(
            year=year, month=month, day=day, coin=coin)

        postgres = DmlCommands(
            db="bitcoin_data",
            user="airflow",
            host="air_postgres_1",
            password="airflow",
            port="5432",
            schema='public')

        postgres.insert_into(response, table='bitcoin_history')
