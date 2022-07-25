import requests


class GetResponse:

    def getDeserialize(self, url: str):

        api_response = requests.get(f'{url}')

        return api_response.json()
