import json
import requests
import ast
from datetime import date, timedelta

class Bitcoin():

    # This function gets data from API 
    def response_get(self, yr: int, month: int, day: int) -> str:

        URL = 'https://www.mercadobitcoin.net/api/BTC/day-summary'

        response_API = requests.get(f'{URL}/{yr}/{month}/{day}')
        
        to_json = response_API.json()

        values =  []

        for column, value in to_json.items():
            values.append(value)

        return values
        

    # This function extracts the values from JSON
    def to_tuple(self, data: str) -> tuple:

        # This method transforms the text into a built-in dictionary
        data_form = ast.literal_eval(data)
        
        return tuple(data_form.values())


if __name__ == '__main__':
    btc = Bitcoin()
    response = btc.response_get(yr=2021, month= 8, day= 25)
    #to_tuple = btc.to_tuple(response)
    print(response)