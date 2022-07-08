from cmath import e
import psycopg2
from tabulate import tabulate


class Postgres_exec():

    def __init__(self, db="projeto-pos", user="postgres", host="localhost", password="123456", port="5433"):
        self.conn = psycopg2.connect(database=db, host=host, port=port, password=password, user=user)
        self.cur = self.conn.cursor()

    
    def insert_into(self, values):

        postgres_insert_query = """ INSERT INTO 
                                projeto.bitcoin_history 
                                ("date_summary",
                                "opening",
                                "closing",
                                "lowest",
                                "highest", 
                                "volume",
                                "quantity", 
                                "amount",
                                "avg_price") 
                                VALUES 
                                (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)"""


        self.cur.execute(postgres_insert_query, values)
        self.conn.commit()


    def select_all(self):

        self.cur.execute(""" SELECT * FROM projeto.bitcoin_history """)
        result = self.cur.fetchall()
        print(tabulate(result, headers=["date_summary",
                                "opening",
                                "closing",
                                "lowest",
                                "highest", 
                                "volume",
                                "quantity", 
                                "amount",
                                "avg_price"], tablefmt='psql'))