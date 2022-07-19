import requests


class GetResponse():

    def getDeserialize(self, url: str):
        
        ApiResponse = requests.get(f'{url}')
        
        toJson = ApiResponse.json()
        
        return toJson


class MercadoBitcoin(GetResponse):

    def __init__(self) -> None:
        #super().__init__()
        self.beginningOfUrl = 'https://www.mercadobitcoin.net/api'


    # This method is to get generally from the API
    def standardGet(self, coin: str, method: str):

        self.URL = f'{self.beginningOfUrl}/{coin}/{method}/'
        
        urlGet = super().getDeserialize(self.URL)

        return urlGet

    
    # This method is to get specifically from the API Day Summary
    def daySummary(self, year: int, month: int, day: int, coin: str):
        
        method = 'day-summary'

        self.URL = f'{self.beginningOfUrl}/{coin}/{method}/{year}/{month}/{day}'

        urlGet = super().getDeserialize(self.URL)

        return urlGet


if __name__ == '__main__':
    pass
