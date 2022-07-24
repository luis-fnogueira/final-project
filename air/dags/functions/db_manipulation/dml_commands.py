from functions.db_manipulation.postgres import Postgres


class DmlCommands(Postgres):

    # In this method we extract the values from JSON and input it into DB.
    def insert_into(self, data: set, table: str) -> None:

        values = tuple(data.values())

        number_of_columns_minus_one = len(values) - 1
        values_parameters_minus_one = '%s, ' * number_of_columns_minus_one

        self.insert_query = f"INSERT INTO {self.schema}.{table} VALUES ({values_parameters_minus_one}%s)"

        self.cur.execute(self.insert_query, values)

        self.conn.commit()
