from functions.get_bitcoin.mercado_bitcoin import MercadoBitcoin
from functions.db_manipulation.dml_commands import DmlCommands


class DaySummaryDag():

    def get_and_input_day_summary(

            self,
            year: int,
            month: int,
            day: int,
            coin: str) -> None:

        """
        This function implements MercadoBitcoin and DmlCommands classes. It uses
        day_summary function from MercadoBitcoin to fetch data.

        Arguments:
            year: integer
            month: integer
            day: integer
            coin: string
        Returns:
            None
            It fetches data and input into database.
        """

        bitcoin = MercadoBitcoin()
        response = bitcoin.day_summary(
            year=year,
            month=month,
            day=day,
            coin=coin
        )

        postgres = DmlCommands(
            db="bitcoin_data",
            user="airflow",
            host="air_postgres_1",
            password="airflow",
            port="5432",
            schema='public'
        )

        postgres.insert_into(response, table='bitcoin_history')
