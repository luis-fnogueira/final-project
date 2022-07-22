import requests


class GetResponse:

    def get_deserialize(self, url: str):

        ApiResponse = requests.get(f'{url}')

        toJson = ApiResponse.json()

        return toJson
