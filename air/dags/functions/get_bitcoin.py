import requests
import ast


class Bitcoin():

    # This function gets data from API 
    def response_get(self, yr: int, month: int, day: int) -> str:

        URL = 'https://www.mercadobitcoin.net/api/BTC/day-summary'

        response_API = requests.get(f'{URL}/{yr}/{month}/{day}')
        
        to_json = response_API.json()

        values =  []

        columns = []

        for column, value in to_json.items():
            values.append(value)
            columns.append(column)

        return columns, values

        

    # This function extracts the values from JSON
    def to_tuple(self, ti) -> tuple:


        # Here we get the value from the last task
        posts = ti.xcom_pull(task_ids=['get_api'])

        # Extracting values from the list
        extracted = posts[0]

        # This method transforms the text into a built-in dictionary
        data_form = ast.literal_eval(extracted)

        # Getting only the values
        values = [x for x in data_form.values()]
        
        return values


if __name__ == '__main__':
    btc = Bitcoin()
    response = btc.response_get(yr=2021, month= 8, day= 25)
    #to_tuple = btc.to_tuple(response)
    print(*response)