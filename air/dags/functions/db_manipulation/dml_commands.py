from functions.db_manipulation.postgres import Postgres


class DmlCommands(Postgres):

    def insert_into(self, data: set, table: str) -> None:
        """
        Extract the values from dict and input it into DB.
        An JSON must be deserialized before calling this function

        Arguments:
            data: a dictionary containing the values
            table: a string (table where data should be sent)

        Returns:
            None
            It executes a query inputting data into a database and commit
        """

        values = tuple(data.values()) 

        number_of_columns_minus_one = len(values) - 1
        values_parameters_minus_one = '%s, ' * number_of_columns_minus_one

        self.insert_query = f"INSERT INTO {self.schema}.{table} VALUES ({values_parameters_minus_one}%s)"

        self.cur.execute(self.insert_query, values)

        self.conn.commit()
