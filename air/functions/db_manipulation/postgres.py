import psycopg2


class Postgres:

    # Constructor method initializing the connection to DB and creating cursor
    def __init__(self, db: str, user: str, host: str, password: str, port: str,
                 schema: str) -> None:

        self.db = db
        self.user = user
        self.host = host
        self.password = password
        self.port = port
        self.schema = schema

        self.conn = psycopg2.connect(
            database=db, host=host, port=port, password=password, user=user)
        self.cur = self.conn.cursor()