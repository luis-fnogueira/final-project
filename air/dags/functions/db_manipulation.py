import psycopg2


class Postgres():

    # Constructor method initializing the connection to DB and creating cursor
    def __init__(self, db, user, host, password, port, schema):
        
        self.db = db
        self.user = user
        self.host = host
        self.password = password
        self.port = port
        self.schema = schema

        self.conn = psycopg2.connect(
            database=db, host=host, port=port, password=password, user=user)
        self.cur = self.conn.cursor()


class CommandsModeling(Postgres):


    # In this method we extract the values from JSON and input it into DB. 
    def insertInto(self, data, table):

        values = tuple(data.values())

        numberOfColumnsMinusOne = len(values) - 1
        valuesParametersMinusOne = '%s, ' * numberOfColumnsMinusOne

        insertQuery = f"INSERT INTO {self.schema}.{table} VALUES ({valuesParametersMinusOne}%s)  "

        self.cur.execute(insertQuery, values)

        self.conn.commit()


if __name__ == '__main__':
    postgres = CommandsModeling(db="bitcoin_data", user="airflow", host="localhost",
                                password="airflow", port="5434", schema='public')
    
    data = {"date":"2022-07-15","opening":111219.96952424,"closing":112193.99983999,"lowest":111015.09208512,"highest":114500,"volume":"5127633.49018562","quantity":"45.34416209","amount":3725,"avg_price":113082.55029629}
    postgres.insertInto(data=data, table='bitcoin_history')
