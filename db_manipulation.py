from cmath import e
import psycopg2


class Postgres_exec:

    @classmethod
    def db_conn(cls):
        
        host = 'localhost'
        port = '5433'
        db = 'projet-pos'
        password = '123456'
        user='postgres'

        try:       
            conn = psycopg2.connect(
                database=db,
                user=user,
                password=password,
                host=host,
                port = port
            )

            print('Connection established!')

        except e:
            print(f'Connection error: {e}')       


    def cursor(self):
        self.db_conn.cursor()

    
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


        self.cursor.execute(postgres_insert_query, values)



