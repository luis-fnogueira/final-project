import requests
import ast



class Bitcoin():

    # This function gets data from API 
    def response_get(self, yr: int, month: int, day: int) -> str:

        response_API = requests.get(f'https://www.mercadobitcoin.net/api/BTC/day-summary/{yr}/{month}/{day}')
        
        data = response_API.text

        return data
        

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
    pass