import get_bitcoin
import db_manipulation


class DaySummaryDag():


    def getAndInputDaySummary(year, month, day, coin):

        bitcoin = get_bitcoin.MercadoBitcoin()
        response = bitcoin.daySummary(year=year, month=month, day=day, coin=coin)

        postgres = db_manipulation.CommandsModeling(db="bitcoin_data", user="airflow", host="localhost",
                                                    password="airflow", port="5434", schema='public')
        
        postgres.insertInto(response, table='bitcoin_history')