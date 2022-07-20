def mocked_connection(*args):
    class MockConn():
        def __init__(self, db, user, host, password, port, schema):
            self.db = db
            self.user = user
            self.host = host
            self.password = password
            self.port = port
            self.schema = schema

    valid_return = ("bitcoin_data", "airflow", "air_postgres_1",
                    "airflow", "5432", "public")

    if args == valid_return:
        return "Connection completed!"
    else:
        return "Invalid arguments!"

if __name__ == "__main__":

    experiment = mocked_connection("bitcoin_data", "airflow", "air_postgres_1",
    "airflow", "5432", "public")
    print(repr(experiment))

    """db="bitcoin_data", user="airflow", host="air_postgres_1",
    password="airflow", port="5432", schema='public'"""