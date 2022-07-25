import psycopg2
from requests import post


class Postgres:

    # Constructor method initializing the connection to DB and creating cursor
    def __init__(self, db: str, user: str, host: str, password: str, port: str,
                 schema: str) -> None:

        self.__db = db
        self.__user = user
        self.__host = host
        self.__password = password
        self.__port = port
        self.__schema = schema

        self.conn = psycopg2.connect(
            database=db, host=host, port=port, password=password, user=user)
        self.cur = self.conn.cursor()

    # Getters of attributes

    @property
    def db(self):
        return self.__db

    @property
    def user(self):
        return self.__user

    @property
    def host(self):
        return self.__host

    @property
    def password(self):
        return self.__password

    @property
    def port(self):
        return self.__port

    @property
    def schema(self):
        return self.__schema

    # Setters

    @db.setter
    def db(self, db):
        self.__db = db

    @user.setter
    def user(self, user):
        self.__user = user

    @host.setter
    def host(self, host):
        self.__host = host

    @password.setter
    def password(self, password):
        self.__password = password

    @port.setter
    def port(self, port):
        self.__port = port

    @schema.setter
    def schema(self, schema):
        self.__schema = schema
