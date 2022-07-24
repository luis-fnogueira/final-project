import requests


class GetResponse:

    def get_deserialize(self, url: str):

        api_response = requests.get(f'{url}')

        return api_response.json()
