from functions.get_bitcoin.get_response import GetResponse


class MercadoBitcoin(GetResponse):

    def __init__(self) -> None:

        """
        Initializing the class with standard endpoint and the class GetResponse
        """

        GetResponse.__init__(self)
        self.__ENDPOINT = 'https://www.mercadobitcoin.net/api'
        self.__URL = ""

    def standard_get(self, coin: str, method: str) -> dict:

        """
        This method is to get generally from the API
        Arguments:
            coin: string
            method: string
        Returns:
            dictionary
        """

        self.__URL = f'{self.__ENDPOINT}/{coin}/{method}/'

        return self.get_deserialize(url=self.__URL)

    def day_summary(self, year: int, month: int, day: int, coin: str) -> dict:

        """
        This method is to get specifically from the API Day Summary
        Arguments:
            year: integer
            month: integer
            day: integer
            coin: string
        Returns:
            dictionary
        """

        METHOD = 'day-summary'

        self.__URL = f'{self.__ENDPOINT}/{coin}/{METHOD}/{year}/{month}/{day}'

        return self.get_deserialize(url=self.__URL)
