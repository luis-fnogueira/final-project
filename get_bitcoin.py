from gettext import bind_textdomain_codeset
import requests
import json


class Bitcoin():

    # This function gets data from API
    def response_get(year: int, month: int, day: int) -> str:

        response_API = requests.get(
            f'https://www.mercadobitcoin.net/api/BTC/day-summary/{year}/{month}/{day}')
        data = response_API.text

        return data

    # This function gets data from response_get and set it to JSON format.

    def to_json(data: str) -> dict:

        data_json = json.loads(data)

        return data_json
