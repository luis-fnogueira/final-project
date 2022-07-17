import requests


class GetResponse():

    def getDeserialize(self, url: str):
        
        ApiResponse = requests.get(f'{url}')
        
        toJson = ApiResponse.json()
        
        return toJson


class MercadoBitcoin(GetResponse):

    beginningOfUrl = 'https://www.mercadobitcoin.net/api'


    # This method is to get generally from the API
    def standardGet(self, coin: str, method: str):

        URL = f'{self.beginningOfUrl}/{coin}/{method}/'
        
        urlGet = super().getDeserialize(URL)

        return urlGet

    
    # This method is to get specifically from the API Day Summary
    def daySummary(self, year: int, month: int, day: int, coin: str):
        
        method = 'day-summary'

        URL = f'{self.beginningOfUrl}/{coin}/{method}/{year}/{month}/{day}'

        urlGet = super().getDeserialize(URL)

        return urlGet


if __name__ == '__main__':
    pass
