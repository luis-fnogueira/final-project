import requests


class GetResponse:

    def get_deserialize(self, url: str):

        """
        It gets data from API and returns it as JSON.
        Arguments:
            url: string
        Returns:
            dictionary of values fetched
        """

        api_response = requests.get(f'{url}')

        return api_response.json()
