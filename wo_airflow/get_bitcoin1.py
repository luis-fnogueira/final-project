from pendulum import yesterday
import requests
import ast
from datetime import date, timedelta

class Bitcoin():

    # This function gets data from API 
    def response_get(self, yr: int, month: int, day: int) -> str:

        response_API = requests.get(f'https://www.mercadobitcoin.net/api/BTC/day-summary/{yr}/{month}/{day}')
        
        data = response_API.text

        return data
        

    # This function extracts the values from JSON
    def to_tuple(self, data: str) -> tuple:

        # This method transforms the text into a built-in dictionary
        data_form = ast.literal_eval(data)
        
        list_values = [x for x in data_form.values()]

        final_vals = tuple(list_values)
        
        return final_vals


if __name__ == '__main__':
    btc = Bitcoin()
    response = btc.response_get(yr=2021, month= 8, day= 25)
    btc.to_tuple(response)