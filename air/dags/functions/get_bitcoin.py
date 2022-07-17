from importlib_metadata import method_cache
import requests


class GetResponse():

    def getDeserialize(self, url: str):
        
        ApiResponse = requests.get(f'{url}')
        
        toJson = ApiResponse.json()
        
        return toJson


class MercadoBitcoin(GetResponse):

    beginningOfUrl = 'https://www.mercadobitcoin.net/api'

    # This function gets data from API 
    def standardGet(self, coin: str, method: str):

        URL = f'{self.beginningOfUrl}/{coin}/{method}/'
        
        urlGet = super().getDeserialize(URL)

        return urlGet

    
    def daySummary(self, year: int, month: int, day: int, coin: str):
        
        method = 'day-summary'

        URL = f'{self.beginningOfUrl}/{coin}/{method}/{year}/{month}/{day}'

        urlGet = super().getDeserialize(URL)

        return urlGet

if __name__ == '__main__':

    daysummary = MercadoBitcoin()
    daysummary.daySummary(coin='BTC', year=2022, month=7, day=16)
