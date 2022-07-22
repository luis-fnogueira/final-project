# Appending our folder with air
import sys
sys.path.append('/air/dags/functions/')
import requests


class GetResponse:

    def get_deserialize(self, url: str):

        ApiResponse = requests.get(f'{url}')

        toJson = ApiResponse.json()

        return toJson
