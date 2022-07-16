# Importing functions
from h11 import Response
from db_manipulation1 import Database
from get_bitcoin1 import Bitcoin

# Instantiating Bitcoin class to get data from API and transform it to a tuple
btc = Bitcoin()

# Setting date to get from the API
response = btc.response_get(yr=2022, month=7, day=11)
print(response)

# Transforming the data receveid from the API to a tuple
normal_tuple = btc.to_tuple(response)
print(normal_tuple)


# Instatiating Database class to interact with the DB
#postgres = Database()

# Inserting into the db the data obtained through the API
#postgres.insert_into(normal_tuple)

# Retrieving data
#postgres.select_all()