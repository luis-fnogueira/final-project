from functions.get_bitcoin import MercadoBitcoin
# from get_bitcoin import MercadoBitcoin
from functions.db_manipulation import CommandsModeling
# from db_manipulation import CommandsModeling

# Appending our folder with functions
import sys
sys.path.append('air/dags/functions')



class DaySummaryDag():


    def getAndInputDaySummary(self, year: int, month: int, day:int , coin:int):

        bitcoin = MercadoBitcoin()
        response = bitcoin.daySummary(year=year, month=month, day=day, coin=coin)

        postgres = CommandsModeling(db="bitcoin_data", user="airflow", host="air_postgres_1",
                                                    password="airflow", port="5432", schema='public')
        
        postgres.insertInto(response, table='bitcoin_history')


if __name__ == '__main__':
    pass
