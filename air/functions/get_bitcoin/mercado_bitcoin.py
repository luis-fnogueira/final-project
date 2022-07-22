from get_response import GetResponse


class MercadoBitcoin(GetResponse):

    # Initializing the class with the standard URL and the class GetResponse
    def __init__(self) -> None:

        self.beginningOfUrl = 'https://www.mercadobitcoin.net/api'
        GetResponse.__init__(self)

    # This method is to get generally from the API
    def standardGet(self, coin: str, method: str):

        self.URL = f'{self.beginningOfUrl}/{coin}/{method}/'

        return self.get_deserialize(url=self.URL)

    # This method is to get specifically from the API Day Summary
    def daySummary(self, year: int, month: int, day: int, coin: str):

        METHOD = 'day-summary'

        self.URL = f'{self.beginningOfUrl}/{coin}/{METHOD}/{year}/{month}/{day}'

        return self.get_deserialize(url=self.URL)
