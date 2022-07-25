from functions.get_bitcoin.get_response import GetResponse


class MercadoBitcoin(GetResponse):

    # Initializing the class with the standard URL and the class GetResponse
    def __init__(self) -> None:

        self.__ENDPOINT = 'https://www.mercadobitcoin.net/api'
        GetResponse.__init__(self)

    # This method is to get generally from the API
    def standardGet(self, coin: str, method: str) -> dict:

        self.URL = f'{self.__ENDPOINT}/{coin}/{method}/'

        return self.getDeserialize(url=self.URL)

    # This method is to get specifically from the API Day Summary
    def daySummary(self, year: int, month: int, day: int, coin: str) -> dict:

        METHOD = 'day-summary'

        self.URL = f'{self.__ENDPOINT}/{coin}/{METHOD}/{year}/{month}/{day}'

        return self.getDeserialize(url=self.URL)
