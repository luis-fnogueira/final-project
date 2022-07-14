"""
This code generate dates to be inputted in Mercado Bitcoin's API.
"""

# Importing our packages
import psycopg2
from db_manipulation1 import Database
from get_bitcoin1 import Bitcoin


# Instantiating classes to use its methods
bitcoin = Bitcoin()
database = Database()

# The start date you want to collect data
year = 2022
month = 3
day = 4


# List with months of the year that have 30 days
monthsWith30Days = [4, 6, 9, 11]

while year < 2023:

    while month < 13:

        while day < 32:
            
                try:

                    # Getting data
                    response = bitcoin.response_get(yr=year, month=month, day= day)
                    print(response)

                    # Parsing its values to insert into DB
                    parsedValues = bitcoin.to_tuple(response)

                    # Inserting into DB
                    database.insert_into(parsedValues)

                    # Increasing day to get next day's data
                    day += 1

                    if day == 31 and month in monthsWith30Days:
                        month += 1
                        day = 1
                    elif day == 32 and month not in monthsWith30Days:
                        month += 1
                        day = 1
                        if month == 12 and day == 32:
                            year += 1
                            month = 1
                            day = 1

                except psycopg2.errors.UniqueViolation as e:
                    continue